package main

// Copyright (c) 2015, Dan Sheffner Digital Imaging Software Solutions, INC
// All rights reserved.
//
// Permission is hereby granted, free of charge, to any person obtaining a
// copy of this software and associated documentation files (the
// "Software"), to deal in the Software without restriction, including
// without limitation the rights to use, copy, modify, merge, publish, dis-
// tribute, sublicense, and/or sell copies of the Software, and to permit
// persons to whom the Software is furnished to do so, subject to the fol-
// lowing conditions:
//
// The above copyright notice and this permission notice shall be included
// in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
// OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
// ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
// SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
// WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
// IN THE SOFTWARE.

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"path/filepath"
	// "reflect"
	"os/exec"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func dump_obj(m *map[string]int) {
	f, err := os.Create("./map.txt")
	check(err)
	for k, v := range *m {
		myString := strconv.Itoa(v) + ",\"" + k + "\"\n"
		_, err := f.WriteString(myString)
		check(err)
	}
	f.Sync()
	f.Close()
	out, err := exec.Command("./sortfile.sh").Output()
	check(err)
	fmt.Printf("%s\n", out)
}

func main() {

	fmt.Println("script started...")

	var files []string
	newline2 := byte('\n')
	numOfLinesProcessed := 0

	// example of creating a map
	m := make(map[string]int)

	root := "../../python/test/"
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		files = append(files, path)
		return nil
	})
	//fmt.Println(files[1:])

	check(err)

	for _, file := range files[1:] {

		// fmt.Println(file)
		file1, err := os.Open(file)
		check(err)
		reader := bufio.NewReader(file1)

		// loop
		for {
			line, err := reader.ReadString(newline2)
			numOfLinesProcessed += 1

			//break out of loop at end of file
			if err == io.EOF {
				break
			}

			// fmt.Println(reflect.TypeOf(line))

			line1 := strings.Split(line, " ")
			ip := line1[0]
			m[ip] += 1

			// fmt.Println(ip)

		}
		file1.Close()
	}
	p := &m

	dump_obj(p)

	fmt.Println("Number of unique IP addresses:")
	fmt.Println(len(m))
	fmt.Println("Number lines processed:")
	fmt.Println(numOfLinesProcessed)
}
