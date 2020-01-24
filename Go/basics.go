package main
import  (
    "fmt"
    "math"
    "runtime"
    "time"
)

// this funciton takes two int parameters and returns one int
func add(x int, y int) int {
    return x + y
}

// a function can return multiple results
func swap(x, y string) (string, string) {
    return y, x
}

// go's return values may be named. If so, they are treated as variables 
// defined at the top of the function.
// a return statement without arguments returns the named return values. 
// this is known as a "naked" return.
// x, y are named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

// the var statement declares a list of variables; as in function argument 
// lists, the type is last.
// a var statement can be at package or function level.
// each variable has default value based on its type
// Variables declared without an explicit initial value are given their zero value.
// The zero value is:
//     0 for numeric types,
//     false for the boolean type, and
//     "" (the empty string) for strings.
var c, python, java bool

// variables with initializers
// a var declaration can include initializers, one per variable.
// ff an initializer is present, the type can be omitted; 
// the variable will take the type of the initializer.
var a, b int = 1, 2
// or simply
// var a, b = 1, 2

// Go's basic types are
//  bool
//  string
//  int int8 int16 int32 int64
//  uint uint8 uint16 uint32 uint64 uintptr
//  byte -- alias for uint8
//  rune -- alias for int32
//          represents a Unicode code point
//  float32 float64
//  complex64 complex128

// -----------------------------------------
// Type conversion
// -----------------------------------------
// The expression T(v) converts the value v to the type T.Some numeric conversions:
// example,
//  var i int = 42
//  var f float64 = float64(i)
//  var u uint = uint(f)

// -----------------------------------------
// Constant
// -----------------------------------------
// constants are declared like variables, but with the const keyword.
// constants can be character, string, boolean, or numeric values.
// constants cannot be declared using the := syntax.
const Pi = 3.14

func sqrt(x float64) string {
    // if statement
    if x < 0 {
        return sqrt(-x) + "i"
    }
    return fmt.Sprint(math.Sqrt(x))
}


func try_defer() {
    // a defer statement defers the execution of a function until the 
    // surrounding function returns. The deferred call's arguments are evaluated 
    // immediately, but the function call is not executed until the surrounding 
    // function returns.
    // output:
    //      hello
    //      hello2
    //      end of try_defer
    defer fmt.Println("end of try_defer")

    fmt.Println("hello")
    fmt.Println("hello2")
}

func main() {
	fmt.Println("hello world")
    fmt.Println(add(42, 13))

    a, b := swap("hello", "world")
    fmt.Println(a, b)

    fmt.Println(split(17))

    var i int
    fmt.Println(i, c, python, java)

    // inside a function, the := short assignment statement can be used 
    // in place of a var declaration with implicit type.
    // try changing the initial value of k and observe how its type is affected.
    k := 3
    fmt.Printf("k is of type %T\n", k)

    // go has only one looping construct, the for loop.
    sum := 0
    for i := 0; i < 10; i++ {
        sum += i
    }
    fmt.Println(sum)

    // ihe init and post statement are optional
    // you can even drop the semicolons
    // for i < 10 { ... }

    // var i1 int = 2
    // if you pass i1 to sqrt(), you will get
    // "cannot use i1 (type int) as type float64 in argument to sqrt"
    // but passing "2" would be fine
    fmt.Println(sqrt(2), sqrt(-4))

    // switch statement
    // switch cases evaluate cases from top to bottom, stopping when a case succeeds.
    switch os := runtime.GOOS; os {
    case "darwin":
        fmt.Println("OS X.")
    case "linux":
        fmt.Println("Linux.")
    default:
        // freebsd, openbsd, windows...
        fmt.Printf("%s.\n", os)
    }

    // another switch example
    today := time.Now().Weekday()
    switch time.Saturday {
    case today + 0:
        fmt.Println("Today.")
    case today + 1:
        fmt.Println("Tomorrow.")
    case today + 2:
        fmt.Println("In two days.")
    default:
        fmt.Println("Too far away.")
    }

    try_defer()
}
