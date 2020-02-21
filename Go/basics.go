// every go program is made up of packages
// programs start runningn in package main
package main

// to use variable, function defined in other package
// use "import"
import  (
    "fmt"
    "math"
    "runtime"
    "time"
    // "mypackage"
)

import "math/rand"

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

    // Deferred function calls are pushed onto a stack. When a function returns, 
    // its deferred calls are executed in last-in-first-out order.
    // so "end 2" will be displayed before "end 1"
    defer fmt.Println("end 1")
    defer fmt.Println("end 2")

    fmt.Println("hello")
    fmt.Println("hello2")
}

func try_pointer() {
    // go has pointers. A pointer holds the memory address of a variable.
    // the type *T is a pointer to a T value. Its zero value is nil.
    var p *int

    // The & operator generates a pointer to its operand.
    i := 42
    p = &i

    // The * operator denotes the pointer's underlying value.
    fmt.Println("*p is ", *p) // read i through the pointer p

    *p = 21 // set i through the pointer p
    fmt.Printf("i is %d", i) // read i through the pointer p
}

func try_struct() {
    type Vertex struct {
        X int
        Y int
    }

    fmt.Println(Vertex{1, 2})

    // struct fields are accessed using a dots
    v := Vertex{1, 2}
    v.X = 4
    fmt.Println(v.X)

    // struct fields can be also accessed through a struct pointer
    p := &v
    p.X = 1e9
    fmt.Println(v)

    // you can list just a subset of fields by using the Name: syntax
    var (
        v2 = Vertex{X: 1}  // Y:0 is implicit
        v3 = Vertex{}      // X:0 and Y:0
        p2 = &Vertex{1, 2} // has type *Vertex
    )

    fmt.Println(p2, v2, v3)
}

func try_array() {
    // the type [n]T is an array of n values of type T
    
    // var a [10]int
    // declares variable "a" as an array of ten integers

    var a [2]string
    a[0] = "Hello"
    a[1] = "World"
    fmt.Println(a[0], a[1])
    fmt.Println(a)

    primes := [6]int{2, 3, 5, 7, 11, 13}
    fmt.Println(primes)

    // an array has fixed size
    // a slice is a dynamically-sized, flexible view into the elements of an array
    // type []T is a lice with elements of type T
    // a slice is formed by specifying two indices, a low and high bound
    // a slice is a half-open range, it does NOT include the high bound, 
    // this is consistent with python, primes[1:4] is more like primes[1:4)
    var s []int = primes[1:4]
    fmt.Println(s)

    // Slices are like references to arrays
    // a slice does not store any data, it just describes a section of an underlying array.
    // changing the elements of a slice modifies the corresponding elements of its underlying array.
    // slices that share the same underlying array will see those changes.
    names := [4]string{
    "John",
    "Paul",
    "George",
    "Ringo",
    }
    fmt.Println(names)

    n1 := names[0:2]
    n2 := names[1:3]
    fmt.Println(n1, n2)

    n2[0] = "XXX"
    fmt.Println(n1, n2)
    fmt.Println(names)

    // a slice literal is like an array literal without the length.
    q := []int{2, 3, 5, 7, 11, 13}
    fmt.Println(q)

    r := []bool{true, false, true, true, false, true}
    fmt.Println(r)

    t := []struct {
        i int
        b bool
    }{
        {2, true},
        {3, false},
        {5, true},
        {7, true},
        {11, false},
        {13, true},
    }
    fmt.Println(t)

    // when slicing, you may omit the high or low bounds to use their defaults instead.
    // the default is zero for the low bound and the length of the slice for the high bound.
    // for the array
    //   var a [10]int
    // these slice expressions are equivalent:
    //   a[0:10]
    //   a[:10]
    //   a[0:]
    //   a[:]

    x := []int{2, 3, 5, 7, 11, 13}
    printSlice(x)

    // Slice the slice to give it zero length.
    x = x[:0]
    printSlice(x)

    // Extend its length.
    x = x[:4]
    printSlice(x)

    // Drop its first two values.
    x = x[2:]
    printSlice(x)

    // slices can be creatd with built-in "make" function
    // make function allocates a zeroed array and returns
    // a slice that refers to this array
    makea := make([]int, 5)  // len(a)=5, cap(a)=5
    makeb := make([]int, 0, 5)  // len(b)=0, cap(b)=5
    printSlice1("makea", makea)
    printSlice1("makeb", makeb)


    // a slice has a length and a capacity
    // length is the number of elements it contains
    // capacity is the number of elements in the underlying array,
    // counting from the first element in the slice 

    // the zero (default) value of a slice is nil
    // a nil slice has a length and capacity of 0 and 
    // has no underlying array
    var emptys []int
    fmt.Println(emptys, len(s), cap(s))
    if emptys == nil {
        fmt.Println("emptys is nil")
    }

}

func printSlice(s []int) {
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

// golang doens't support funciton overloading
// I have to give it a different name
func printSlice1(s string, x []int) {
    fmt.Printf("%s len=%d cap=%d %v\n", s, len(x), cap(x), x)
}

func try_range() {
    // the range form of the for loop iterates over a slice or map.
    // when ranging over a slice, two values are returned for each iteration. 
    // the first is the index, and the second is a copy of the element at that index.

    var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

    for i, v := range pow {
        fmt.Printf("2**%d = %d\n", i, v)
    }

    // initialize the slice
    pow = make([]int, 10)
    // populate the slice
    for i := range pow {
        pow[i] = 1 << uint(i) // == 2**i
    }

    // You can skip the index or value by assigning to _.
    for _, value := range pow {
        fmt.Printf("%d\n", value)
    }
}

func try_map () {
    // a map maps keys to values.
    // the make function returns a map of the given type, initialized and ready for use.
    type Vertex struct {
        Lat, Long float64
    }

    // key is a string, value is a Vertex struct
    var m map[string]Vertex

    m = make(map[string]Vertex)
    m["Bell Labs"] = Vertex{
        40.68433, -74.39967,
    }
    fmt.Println(m["Bell Labs"])

    // map literals are like struct literals, but the keys are required
    var m2 = map[string]Vertex{
        "Bell Labs": Vertex{
            40.68433, -74.39967,
        },
        "Google": Vertex{
            37.42202, -122.08408,
        },
    }

    fmt.Println(m2)

    // to insert or update an element in map m:
    // m[key] = elem

    // to retrieve an element:
    // elem = m[key]

    // to delete an element:
    // delete(m, key)

    // to test that a key is present with a two-value assignment:
    // elem, ok := m[key]
    // if key is in m, ok is true. If not, ok is false.
    // if key is not in the map, then elem is the zero value for the map's element type.

    m3 := make(map[string]int)

    m3["Answer"] = 42
    fmt.Println("The value:", m3["Answer"])

    m3["Answer"] = 48
    fmt.Println("The value:", m3["Answer"])

    delete(m3, "Answer")
    fmt.Println("The value:", m3["Answer"])

    v, ok := m3["Answer"]
    fmt.Println("The value:", v, "Present?", ok)
}

// ------------------------------------------------------------------------
// function value
// ------------------------------------------------------------------------

func try_function_value() {
    // functions are values too. They can be passed around just like other values.
    // function values may be used as function arguments and return values.

    // hypot refers to a function which take two float64 as arguments
    // and returns float64
    hypot := func(x, y float64) float64 {
        return math.Sqrt(x*x + y*y)
    }
    fmt.Println(hypot(5, 12))

    // pass hypot function to compute as argument
    fmt.Println(compute(hypot))
    fmt.Println(compute(math.Pow))
}

// compute is a function which takes a function value as argument
// and returns a float64
// function value "func(float64, float64) float64" means it takes
// two float64 as arguments and returns float64  
func compute(fn func(float64, float64) float64) float64 {
    return fn(3, 4)
}

// ------------------------------------------------------------------------
// function closure 
// ------------------------------------------------------------------------

// go functions may be closures. a closure is a function value that 
// references variables from outside its body. 

// the adder function returns a closure, each closure is bound to its own
// sum variable. in this specific case, the closure is a function value
// which take a int and return int

func adder() func(int) int {
    sum := 0
    return func(x int) int {
        sum += x
        return sum
    }
}

func try_function_closure () {
    // adder() returs a function closure, which is assigned
    // to pos
    pos := adder()

    // all the pos() function calls reference the same "sum" variable
    // "sum" acts like a static variable
    // sum = 0 + 0 + 1 + 2 + 3 + 4 ...
    fmt.Println("calling pos() in try_function_closure")
    for i := 0; i < 10 ; i++ {
        fmt.Println(pos(i))
    }
}

// ------------------------------------------------------------------------
// method
// ------------------------------------------------------------------------

// go doesn't have classes, however, you can define
// methods on types.
// a method is a function with speicial receiver argument
type Vertex struct {
    X, Y float64
}

// method can ONLY be defined at the package level, it 
// can't be defined inside a function
// Abs() is a method which has a receiver of type Vertex named v
// Abs() doesn't take any argument, and returns float64
func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// you can also declare a method on non-struct type
// you can only declare a method with a receiver whose type
// type is defined in the same package as the method. you can
// not declare a method with a receiver whose type is defined
// in another package (which incudes built-in types such as float64)
// the following is the workaround
type MyFloat float64
func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

// you can declare a method with pointer receiver
// methods with pointer receiver can modify the value to which
// the receiver points
// see the following examples of pointer receiver vs
// value receiver
func (v *Vertex) Scale (f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}

// with a value receiver, the NoScale() emthod operates on
// a copy of the orignal v
func (v Vertex) NoScale (f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}

func try_method() {
    v := Vertex{3, 4}
    // call Abs() method on Vertex object v
    fmt.Println("Abs() method on Vertex", v.Abs())
    
    // call Abs() regular function
    fmt.Println("regular Abs() function", Abs(v))

    // call Abs() method on MyFloat
    f := MyFloat(-math.Sqrt2)
    fmt.Println("Abs() method on MyFloat", f.Abs())

    // call Scale() method
    fmt.Println("before calling Scale() method v is", v)
    v.Scale(10)
    // v has been changed by Scale()
    fmt.Println("after calling Scale() method v is", v)

    v.NoScale(2)
    // v doesn't change
    fmt.Println("after calling NoScale() method v is", v)

    // call cale() function
    Scale(&v, 2)
    fmt.Println("after calling Scale() function v is", v)
}

// as comparison, this is what the regular function look like
func Abs(v Vertex) float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// this is Scale method rewritten as regular function
func Scale (v *Vertex, f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}

// ------------------------------------------------------------------------
// interface
// ------------------------------------------------------------------------

// an interface type is defined as a set of of method signatures
// a value of interface type can hold any value that implements
// those methods
 
type Abser interface {
    Abs() float64
}

func try_interface() {
    var ai Abser
    // ai is a value of Abser interface type
    // so it can hold anything that implements Abs() method

    // in the method section above, we already defined
    // Abs() method on MyFloat, Vertex, *Vertex
    // a type implements an interface by implementing its
    // methods. there is no explicit declaration of intent,
    // no "implements" keywords on the type, this is referred
    // as duck-typing

    // under the hood, interface value can be thought of as
    // a tuple of a vlaue and a concrete type
    // (value, type)
    // calling a method on an interface value executes the method
    // of the same name on its underlying type

    f := MyFloat(-math.Sqrt2)
    v := Vertex{3, 4}

    ai = f
    describe(ai)
    fmt.Println(ai.Abs())
    
    ai = v
    describe(ai)
    fmt.Println(ai.Abs())
}

func describe(ai Abser) {
    fmt.Printf("(%v, %T)\n", ai, ai)
}

// ------------------------------------------------------------------------
// Stringer interface
// ------------------------------------------------------------------------

// Stringer interface is defined by fmt package
// a Stringer is a type that can describe itself as a string
// the fmt package look for this interface to print values

type Person struct {
    Name string
    Age int
}

// in order for Println to print a value of Person type
// there needs to be "String()" method on Person type
func (p Person) String() string {
    return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

func try_stringer() {
    a := Person{"Authur Dent", 42}
    z := Person{"Zaphod Beeble", 90}
    fmt.Println(a, z)
}

// ------------------------------------------------------------------------
// error interface
// ------------------------------------------------------------------------

// the error type is a built-in interface similar to fmt.Stringer
// function often retun an error value, calling code should test whether
// the errro value equal nil
// an nil error means success, a non-nil error denotes failure

type MyError struct {
    When time.Time
    What string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("at %v, %s", e.When, e.What)
}

func run_something() error {
    // doing something

    // create a MyError value and return its pointer
    return &MyError {
        time.Now(),
        "it didn't work",
    }

    // note: if you put MyError definition in one line
    // you don't need to put a "," after "it didn't work"
    // return &MyError { time.Now(), "it didn't work" }

}

func try_error () {
    if err := run_something(); err != nil {
        fmt.Println(err)
    }
}

// ------------------------------------------------------------------------
// goroutine
// ------------------------------------------------------------------------

// a goroutine is a lighweight thread managed by the Go runtime
// go f(x, y, z)
// starts a new goroutine running f(x, y, z)
// the evalution of f, x, y, and z happens in the current goroutine
// the exeuction of f(x, y, z) happens in the new goroutine

// goroutines run in the same address space, so access to shared
// memory must synchronize
func say(s string) {
    for i := 0; i < 5; i++ {
        time.Sleep(20 * time.Millisecond)
        fmt.Println(s)
    }
}

func try_goroutine() {
   go say("world")
   say("hello")
}

// ------------------------------------------------------------------------
// buffered channel
// ------------------------------------------------------------------------

// Channels can be buffered. Provide the buffer length as the second argument
// to make to initialize a buffered channel:
// ch := make(chan int, 100)
// Sends to a buffered channel block only when the buffer is full. 
// Receives block when the buffer is empty.

func try_buffered_channel() {
    ch := make(chan int, 2)
	ch <- 1
    ch <- 2
    // overfill the channel will give error like the following
    // "fatal error: all goroutines are asleep - deadlock"
	// ch <- 3
	fmt.Println(<-ch)
    fmt.Println(<-ch)
    // similarly, over-drain the channel will also give fatal error
	// fmt.Println(<-ch)
}

func fibonacci(n int, c chan int) {
    x, y := 0, 1;
    for i := 0; i < n; i++ {
        fmt.Println("send fibonacci value: ", x)
        c <- x
        x, y = y, x + y
    }
    close (c)
}

func try_close_range() {
    // a sender (and only sender) can  close the channel to indiciate that
    // no more values will be sent.
    // receiver can test whether a channel has been closed by
    // v, ok := <-ch
    // ok is false if there are no more values to receive and the channel
    // is closed
    // the loop "for i := range c" receives values from  the channel repeatedly
    // until it is closed

    c := make(chan int, 10)
    // this is goroutine, so we don't wait for the channel to be full
    // to receive the values
    go fibonacci(cap(c), c)
    for i := range c {
        fmt.Println("receive fibonacci value: ", i)
    } 
}


// ------------------------------------------------------------------------
// binary tree
// ------------------------------------------------------------------------

type Tree struct {
    Left *Tree
    Value int
    Right *Tree
}

// to create a binary tree
// k is the multiplication factor
// rand.Perm(n) returns a slice of n random integers whose
// values are between 0 and n, [0,n)
// e.g. 
// rand.Perm(10) returns
//  [9 4 2 6 8 0 3 1 7 5]
func New(n, k int) *Tree {
    var t *Tree
    n1 := rand.Perm(n)
    fmt.Println("rand.Perm(n) retrns ", n1)
    for _, v := range n1 {
        fmt.Println("insert value ", v, "to tree")
        t = Insert(t, (1+v)*k)
    }
    return t
}

// insert a value to the binary tree
func Insert(t *Tree, v int) *Tree {
  return t
}
 
func try_tree() {
    t1 := New(10, 1)
    fmt.Println("t1 value is", t1.Value)
}

func main() {
	fmt.Println("hello world")
    fmt.Println(add(42, 13))

    a, b := swap("hello", "world")
    fmt.Println(a, b)

    fmt.Println(split(17))

    var i int
    // see declaration of c, python, java above
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

    try_pointer()

    try_struct()

    try_array()

    try_map()

    try_function_value()

    try_function_closure()
    
    value_vs_ref()

    try_range()

    try_method()

    try_interface()

    try_stringer()

    try_error()

    try_goroutine()

    try_buffered_channel()
    
    try_close_range()

    try_tree()
}

// the order of the function doens't matter
// function can be defined after where it is called
func value_vs_ref () {
    var a int = 1
    // b is copy of a
    var b = a
    // c is reference to a
    var c = &a
    fmt.Println(a, b, *c)

    // changing b will not change a
    b = 2
    // changing *c will change a
    *c = 3
    fmt.Println(a, b, *c)
}

