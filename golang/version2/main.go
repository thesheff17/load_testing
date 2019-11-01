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
			x += 1
		}
	}

	fmt.Println("Number of unique IP addresses:")
	fmt.Println(len(m))
	fmt.Println("Number lines processed:")
	fmt.Println(numOfLinesProcessed)
}
