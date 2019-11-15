// Copyright (c) Dan Sheffner Digital Imaging Software Solutions, INC
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

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type entry struct {
	val int
	key string
}

type entries []entry

func (s entries) Len() int           { return len(s) }
func (s entries) Less(i, j int) bool { return s[i].val < s[j].val }
func (s entries) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

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
			numOfLinesProcessed++

			//break out of loop at end of file
			if err == io.EOF {
				break
			}

			// fmt.Println(reflect.TypeOf(line))

			line1 := strings.Split(line, " ")
			ip := line1[0]
			m[ip]++

			// fmt.Println(ip)

		}
		file1.Close()
	}

	fmt.Println("building struct for sort...")
	var es entries
	for k, v := range m {
		es = append(es, entry{val: v, key: k})
	}

	sort.Sort(sort.Reverse(es))

	x := 1
	for _, e := range es {
		fmt.Printf("%q : %d\n", e.key, e.val)
		if x > 9 {
			break
		} else {
			x++
		}
	}

	fmt.Println("Number of unique IP addresses:")
	fmt.Println(len(m))
	fmt.Println("Number lines processed:")
	fmt.Println(numOfLinesProcessed)
}
