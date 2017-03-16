package main

import "errors"
import "fmt"

func f1(args int) (int, error)  {
    if arg == 42 {
        return -1, errors.New("cant work with 52")
    }

    return arg + 3, nil
}
