# Go Prymer - Speaker notes

> This document contains a summary of the speaker notes used to present this talk to accompany the [pdf snapshot of the slides](go-prymer.pdf)

- [Go Prymer - Speaker notes](#go-prymer---speaker-notes)
  - [1 - Title page](#1---title-page)
  - [2 - Contents](#2---contents)
  - [3 - Let's say hello to the world (title)](#3---lets-say-hello-to-the-world-title)
  - [4 - Let's say hello to the world (example)](#4---lets-say-hello-to-the-world-example)
  - [5 - Let's get running](#5---lets-get-running)
  - [6 - What about virtual envs?](#6---what-about-virtual-envs)
  - [7 - Who goes where?](#7---who-goes-where)
  - [8 - Comparing Layouts](#8---comparing-layouts)
  - [9 - The (almost) simplest Go project](#9---the-almost-simplest-go-project)
  - [10 - A common approach](#10---a-common-approach)
  - [11 - How many pacakges?](#11---how-many-pacakges)
  - [12 - Good package names](#12---good-package-names)
  - [13 - What no while?](#13---what-no-while)
  - [14 - The fundamentals](#14---the-fundamentals)
  - [15 - It's all for one, and one for all!](#15---its-all-for-one-and-one-for-all)
  - [16 - You're just my type - dictionaries == maps](#16---youre-just-my-type---dictionaries--maps)
  - [17 - You're just my type too - lists == arrays/slices](#17---youre-just-my-type-too---lists--arraysslices)
  - [18 - Strctural anatomy](#18---strctural-anatomy)
  - [19 - Don't be classy](#19---dont-be-classy)
  - [20 - Structural composition](#20---structural-composition)
  - [21 - Where are my getters?](#21---where-are-my-getters)
  - [22 - Don't be exceptional](#22---dont-be-exceptional)
  - [23 - The special stuff](#23---the-special-stuff)
  - [24 - Marshaling](#24---marshaling)
  - [25 - Cross compilation](#25---cross-compilation)
  - [26 - Ensure stuff happens with defer()](#26---ensure-stuff-happens-with-defer)
  - [27 - Concurrency with Go routines](#27---concurrency-with-go-routines)
  - [28 - Channels](#28---channels)
  - [29 - Coding with style](#29---coding-with-style)
  - [30 - The zen of python](#30---the-zen-of-python)
  - [31 - Let's print the elements of a list (z) and their index](#31---lets-print-the-elements-of-a-list-z-and-their-index)
  - [32 - What about something similar in Go?](#32---what-about-something-similar-in-go)
  - [33 - Start with simplicity](#33---start-with-simplicity)
  - [34 - Any final thoughts?](#34---any-final-thoughts)
  - [35 - Any questions?](#35---any-questions)
  - [36 - About me](#36---about-me)
  - [37 - See also](#37---see-also)

## 1 - Title page

Welcome to Go for Python engineers!

In this talk I’ll attempt to give you a bit of a flavour of Go and compare and contrast to what you’d expect in your daily python workflow

This isn’t a complete Go tutorial - there are much better ones out there!

## 2 - Contents

We’re going to run through:

1. A quick Hello World comparison
2. A run through common project layout
3. Some more in depth comparison between some core features of the languages
4. A run through some of the things that will be new to you in Go
5. Idiomatic Go and style
6. Then if there’s time, questions!

There’s a lot to cover, so let’s Go!

## 3 - Let's say hello to the world (title)

So let’s start with a little hello world to see how things look in both languages

## 4 - Let's say hello to the world (example)

Here’s a little hello world in both Python and Go

**Some points of interest**

The similar:

- **Imports**
  - both declare things they import
  - python with from/import, Go with import 
  - python may import functions and call them as though local; Go always prefixes imported functions with the package name

- **Semicolons**
  - neither uses semicolons as statement terminators! Yay!

- **Auto-docs**
  - as python has pydoc (triple “ comment), Go has godoc
Only public items should be documented (enforced by linters)

The differences:

- **Package declaration**
  - all go code files begin with a package declaration

- **Typing**
  - python is dynamically typed, Go is strongly typed

- **Entry point**
  - the main function is the entry point to the every Go program
unlike the python main() here, Go’s main function must always be called main, can’t take any args and returns nothing

- **Visibility**
  - python does not enforce access levels (public, private), Go does
python usually uses convention such as underscores
Go uses Upper and Lowercase letters (enforced by compiler)
Public is visible to your whole program. Private is only within the package

- **Code blocks**
  - python uses indentation, like java/C, Go uses curly brackets to define code blocks instead of python’s indentation

## 5 - Let's get running

Let’s run our Hello World from the last slide

The general experience of running Go and python is pretty similar and just as quick as you can see from the examples

The main difference is that Go is a compiled language rather than interpreted

- The `build` command will output a native binary (more on that later!)
- The `run` command will **compile** and **run** in a single step

Unlike some languages when you may expect the **build** to be appreciably longer than just **run**, in practice you’ll never notice the difference.

Most Go code will compile in <1s and once compiled will start up incredibly fast!

> Note! Timestamps correct at time of writing! 

## 6 - What about virtual envs?

But what about virtual envs?

With Go, there’s no need to use a virtualenv to allow different projects on your machine to use different versions of a dependency

- The go modules system takes care of managing dependencies and isolating versions on disk
- Similar to Pipfile or Requirements.txt, go.mod and go.sum lock dependency versions
- No third party tools required! This is all built into the standard Go toolchain and workflow

## 7 - Who goes where?

A word about project layout

Some languages impose a fairly rigid structure on code layout, but Go doesn’t

Go does have some best practice and conventions, but the only really enforced things are:

- **Packages are defined by folders** - no two files with different package declarations (with the exception of *_test) may share a folder
- **Every non-library program must have a main package**

> Note! The colouring in the following examples is just for easy comparison of layouts

## 8 - Comparing Layouts

Let’s start with a comparison

Left is example python, right is rough equivalent Go

- **Main** entry point (here: main.go for Go, and app.py for python)

- **Packages** - (`api` and `data`)
  - Python requires __init__.py files to treat folders as packages
  - In Go, a folder itself defines the package (along with the package declaration)

- **Tests**
  - Python (and others), usually live in Test folder
  - In Go, live alongside the code they test in Go rather than in a separate folder
  - Always called `<something>_test.go`
  - In the same folder means in the same package
  - However, you can optionally use a special convention (package name suffixed with `_test`) which allows you to test the public api of your package as if you were in another (this is the only exception to the only one package per folder rule)

- **Dependencies** - In this case, python is using Pipfile although other things are available. For Go, we use Go modules which are defined using `go.mod` and `go.sum`
Roughly:
  - `go.mod` == `Pipfile`
  - `go.sum` == `Pipfile.lock`

## 9 - The (almost) simplest Go project

In this example all the code for the project lives in a single folder under `package main`

> NOTE ON COMPILING IN ONE FOLDER: e.g. “go build main.go api.go data.go”

It could just as easily be a single `*.go` file (which is the best place to start) but in this case, the functions to do with authorization have been split into a separate file for ease of reading - as far as Go is concerned it’s all one.

Looking at the path

- You can develop/checkout and run a go project from any location
- I tend to favour keeping them under the same path as their version control location (usually under a top level git/ folder)

## 10 - A common approach

This is a layout you’ll probably see a fair bit in Go repos

- `cmd/` - The main.go for the program (or multiple main’s) live under here.
  - E.g. you may have a service that can run as a command line app or a webservice. In this case you’d separate them under cmd/ allowing them to be built separately but share common library code
  - If you’ve only got the one service, then cmd/ may be more than you require

- `Internal/` and `pkg/` - these are where other packages local to the project live
  - `pkg/` is for code that can be shared with other projects. It can be imported from here via go modules without needing to import the whole project
  - `internal/` is used for code that you want to share between apps in cmd/ but not share outside the project. This is one of the few magic parts of Go, as the non-external visibility of packages under internal/ is enforced by the compiler

> Note! The packages shown are arbitrary and not in any particular folder for any reason

## 11 - How many pacakges?

A common mistake (I certainly made it early on!) is to split your packages the way you’d split libraries or classes in other languages

Go’s packages are more like namespaces and in most cases there’s nothing to stop you putting everything in main!

_(refer to slide)_

And now a quick word on naming (_next slide_)

## 12 - Good package names

Good package names:

- Are short and concise
- Should compliment their public functions and types - this means they read smoothly like `list.Add()`
- Should not “stutter” in conjunction with good function names - that is `client.New()` is a good name, `client.NewClient()` is not
- And you should avoid “meaningless” names, such as `util` or `common` that convey no context to the user

## 13 - What no while?

So, what about the code itself you ask?

Again I’m not going to attempt to teach you all of Go here (check the tour of go for a great introduction!), but let’s look at what’s similar, and what’s different

## 14 - The fundamentals

Let’s start by comparing some fundamentals in both languages

**Variables:**

You’ll notice a lot of the declarations look very similar, however they are:

- **strongly typed** and must declare their types before being used.
- declared syntactically **backwards** as far as languages like java are concerned e.g. `public int myNumber;`
- can be explicitly declared with var at which point, unless they are assigned, take the default empty value for their type
- **hippo operator** ( colon-equals ) which infers the type from the value - look quite similar to declarations in python, and are really useful when calling functions!
  - A hippo is not a walrus - be careful not to get caught out thinking they do the same thing!
  - unlike python, when a variable is declared, it’s value may change, but it’s type may not

**Functions**

- are similarly strongly typed:
- may return zero or more values
- arguments to functions in Go are pass-by-value

As already touched upon, the public or private visibility of variables and functions is defined by the upper or lowercase-ness of the the first character. Public items can be seen from anywhere in the program. Private items are only visible within their package. There is no protected!

**Nothing**

And last but not least, null values that would be `None` in python are `nil` in Go!

## 15 - It's all for one, and one for all!

**Looping**

Go only has one loop construct - `for` (it’s also one of the very few places you’ll find semicolons in Go)

That may sound limiting, but it isn't! The for can simulate any other loop you like just by changing its parameters.

At the heart, it’s a standard c-style for, with an initialiser, condition and iterator expression. By using or removing these you can craft the other loop behaviours.

- **Enumerate** - the equivalent is Go’s `range` (different to python’s!). Be aware that the range will return a copy of the value, not the value itself. Be wary of this when you want to mutate the value! If you need a reference to the actual value, use the c-style for and access via index (or use the keys to access elements for maps)

- **C Style While** - a `while` in Go is just a for that’s omitted it’s initializer and iterator
Could also be (including the iterator):

  `For ; i < len(z); i++ {} // Note the leading semicolon!`

- **To infinity and beyond!** - In other languages you need to still supply a condition to loop until. In Go, if you omit all the parameters then the compiler knows you want to just go forever!
Standard break statements and such can be used to break out when you need to!

## 16 - You're just my type - dictionaries == maps

**Dictionaries**

The closest analogy to a python dictionary is a map - _don’t get this confused with a `map()` function!_

- In **go**, the types for key and value must be declared and may not change
- In **python**, keys and values may be anything - in go they must be all the same type
  - A technical exception to this is by using interfaces - although these are still types!
  - These are very powerful
  - Though don’t use them as an excuse to try and avoid typing properly!

**Maps** can be iterated with the `range` operator where it gives key and value.

## 17 - You're just my type too - lists == arrays/slices

**Lists**

The closest analogy to a python list is an array or slice - you’ll usually see slices a lot more in Go than arrays, though that doesn’t mean arrays are never used

There’s too much to go into depth of slices here, but for now, think of them as lightweight windows over the top of real arrays

A few notes:

- **Arrays** are defined by having a fixed size in the square brackets. Arrays cannot change size without memory allocation
- **Slices** are defined without a size in the brackets. The can either be initialised as empty; with a set of values or pre-sized/allocated using make
  - Make takes two values in addition to the type (the second of which is optional) - initial size and allocated size. If allocated size is omitted it is set to the length
  - If size is non-zero, the elements up to that length are populated with the default zero-value for the array’s declared type.
- Initialised elements in a slice or array may be accessed/set via index
- Other utility functions such as append exist for efficient manipulation of slices
- A slice may be re-sized within it’s allocated bounds without memory allocation. Only growing beyond its current limit will cause a reallocation
- **WARNING!** Multiple slices can point to the same data - only a reallocation or explicit copy will break that association so be mindful of what you’re changing (or when you think you are, but are now on a copy) 

Like **maps, arrays** and **slices** can also be iterated with the `range` operator where it gives index and value.

## 18 - Strctural anatomy

A quick look at structs before we go further

If you’re familiar with C or similar then you may have seen things like this before.
Otherwise if this is new, a struct is a fixed data structure - once declared its field values may change, but its structure may not

Let’s look at this one:

- It’s declared as a type called, in this case, Basket 
- It’s public as denoted by the uppercase letter
- Each field is declared on a new line and must have a type
- Again, ID, Total and Items are public; paid is private
- ID and Total also declare here what’s know as struct tags
  - These have several uses (and you create your own!) although the most common is for marshaling and unmarshaling to and from JSON (as in this case, or YAML, or any other format) - more on that later
- Struct fields can also be other structs (or any valid type)!

## 19 - Don't be classy

So, structs look a little like classes - but Go isn’t Object Oriented!

Don’t write OO Go - you’ll have a bad time!

But let’s look at a rough equivalent as there are some similarities


Essentially the Go example is just a struct (Dog) - although a struct may have behaviour through the use of functions with what’s known as a receiver type (which lives between the func declaration and function name)

At a high level:

- `Dog` is a **public** struct (uppercase first letter, so it’s visible to the whole program)
- `Bark()` is a **public** function (similarly uppercase first letter) which accepts a Dog as a receiver (similar to how a class method takes self). Fleas is a private function (lowercase first letter) visible outside of the struct, but only within the package. In this case the receiver is a value type, which means the function cannot mutate it.
- It’s worth noting that although you can, you usually don’t mix pointer and value receiver types!
- Also, there is no such thing as inheritance in Go!

The full ins and outs of receiver types and, by association interfaces are beyond the scope of this talk, but tour.golang.org etc cover them pretty well

Though speaking of structs and interfaces… (next slide)

## 20 - Structural composition

Let’s have a bit more of an advanced look at structs

In this case we have three structs:

- An `animal` that has a single public field
- A `dog` that has public walkies
- A `cat` that has private lives
- Both also contain an `animal` - but it has no type? What’s going on there?

**Inheritance**

As previously mentioned there is no inheritance in Go. What it has instead is composition.

In the example, the fields and and behaviours of animal are embedded into dog and cat. This looks a little like inheritance but it really isn’t. As previously noted do not try to write object oriented Go!

It’s worth noting that in most Go code you’ll never see or use composition, but it’s good to be aware of!

**Interfaces**

Another one that is likely to catch out those from an OO background are interfaces. In Go, a struct never explicitly implements an interface. There is no implements keyword. An interface is satisfied implicitly by just having the right behaviour.

In the above example, the dog struct satisfies the petter interface as it implements the `Pat()` function. The cat does not. However, if cat had a `Pat()` added, it would now satisfy the interface too!

> **Note!** In the example, the structs are being created with an ampersand - this is returning a pointer instead of a value. To create just a value and get it directly, drop the ampersand. We’re using it here, as `Pat()` expects a pointer receiver.
Don’t worry too much about pointers - in Go most of the time the compiler will take care of things - they’re not the mind-bending things they are in C!

## 21 - Where are my getters?

Another mindset change

It’s common to try and treat structs as classes and so feel you need getters and setters

This is not true of Go. The correct way is to access fields directly

That said, it doesn’t mean you’ll never have a need for them - there are absolutely cases where access to fields is better done via a function.

However, if you’re about to create one, think about whether it’s really necessary

## 22 - Don't be exceptional

Go doesn’t have exceptions. Instead it has explicit errors.

Why is this a good thing?

Well you should always handle errors - if you don’t, who will?

But, I hear you say, we handle exceptions too? Well you can, but you don’t have to - it’s easy to throw an exception or just let something else throw one up the stack and hope someone somewhere will deal with it - that’s where all those Unhandled Exception Exceptions come from!

So why are explicit errors better?

- in Go you’re forced to handle them there and then. They can’t slip by unhandled, and you have all the context you need to deal with them effectively.
- exceptions are often abused to control code flow rather than actually being exceptional.
- `try ... except` blocks can be very large with a lot of potential points it could quit unexpectedly
- it means you don’t have to spend time parsing stack traces - the cause of an error should be explicit!

A downside to Go’s errors, is that they are, as you can see from the example, fairly verbose - you’ll see if err != nil a lot! - but it’s also a strength. There’s no magic where an exception can pull you out of an execution flow midway which can make debugging a pain.

In the example above, the python attempts to do everything and hopefully catches when things go wrong. With the Go, it stops (metaphorically!) and checks after every call to ensure everything’s okay!

Not so much here, but a lot of things you may have needed to use exceptions for in python are caught by the compiler in Go so would never make it as far as run time.

## 23 - The special stuff

And now for a lightning tour of more stuff that’s specific to Go!

Not going into depth, but you can learn more about these things on the Go tour

So without further ado (next slide)

## 24 - Marshaling

Needing to marshal to and from JSON (and other data formats) is a common operation in modern software - and Go has you covered!

Simply run a struct through a marshaler and the fields will be mapped to your data format (or vice versa!).

Most marshalers will also support marshaling to and from other types such as maps, but structs are the more common case

By default, public fields will all be marshaled, private will not
Fields in the JSON will be named as the fields in the struct - unless overridden as shown using struct tags

## 25 - Cross compilation

With other traditional compiled languages, you need to compile code on the platform you want the binary to run on.

With Go, you can build for any supported platform from wherever you write your code - simply with compiler flags passed to build

This means you can build on a macbook and get a binary to run on ubuntu, windows or even a raspberry pi amongst others! This is especially cool for when you’re building for cloud functions or containers that will run on different architectures to your development machine.

## 26 - Ensure stuff happens with defer()

Always forgetting to close resources? Let `defer()` do it for you!

Similar to a _finalise_, `defer` ensures the given function will execute when it falls out of scope.

In the above, once we know the new file has been created correctly, we defer closing it and let Go take care of it.

The code is a simple case, but imagine having lots of logic and possible returns in the function. defer ensures, that the file will always attempt to be closed without us needing to remember to do it everywhere.

A `defer()` will even run if your code `panic()`’s!

This leads to cleaner and safer code

## 27 - Concurrency with Go routines

Go is concurrent by design. This differs from many languages where concurrency and asynchronous operation are add ons.

Implemented with **goroutines**

- The main thread is also just another goroutine!
- **green threads** - scheduled by the runtime rather than the underlying OS
- **Lightweight** - the runtime can run 1000s of goroutines at once for very little cost (compared to say, java threads)

_(refer to example)_

In the code shown, the first example runs sequentially.
The second runs concurrently - just with the addition of the `go`

There’s a little bit more to it than that as, in the example, the program will, without anything else, exit almost immediately.

Once a goroutine is spawned it is independant of the goroutine that spawned it
You must implement a _waiting pattern_ (of which there are many) to ensure you actually wait for them to finish (or not if you don’t need to!)

You should never use a goroutine to share memory (variables) directly - you should always share memory by communicating, and for that we use channels (next slide)

## 28 - Channels

Now you have things running concurrently, you need to be able to return data

In most other languages this needs to be carefully coordinated to avoid race conditions writing to memory

In go, we use **channels**

- **Simple queues** - can be one-in-one-out or buffered as needed

(refer to example)

Here we make a simple channel of type int (remember, Go is strongly typed so everything needs a type! - but this could just as easily be struct or func!)

The channel is passed to the function as a normal argument

The function then just writes it’s result to the channel

The `result := <- c` declares an integer variable (inferred from the channel!) and blocks waiting for a value on the channel.

Once received the value is assigned to **result** and the program continues

----

(BONUS)

Go does have mutexes under the hood (and you can use them directly if you do need), but in the most part, Go does the hard work for you!

## 29 - Coding with style

A phrase you’ll hear a lot when working with Go is “Idiomatic Go” and a lot of engineers new to Go tend to say “what’s that all about?”

It could be equated to “the right” way to code Go, although that sounds a little prescriptive.
It’s more like the “expected” or “best practice” way to code Go

That is, if someone is reading your code, it’s a consistent approach and style that should be familiar to them (note: code formatting is part of this; but this isn’t just formatting!)

Un-idiomatic Go is not wrong, but writing idiomatic Go is important for clear, concise and effective code

But what about Python?

## 30 - The zen of python

You’re probably already using idiomatic python!

Though I’ve heard “idiomatic” a lot less with regard to python, the same principals (which you no doubt already follow!) apply

This is an exact from The Zen of Python which sums it up (read from slide)

## 31 - Let's print the elements of a list (z) and their index

Let’s look at a quick example - printing the elements of an array and their indexes

(refer to slide)

## 32 - What about something similar in Go?

And indeed with Go, there’s more than one way to do it as we can see

Caveat: Remember that range gives a copy of the value. So if you want to mutate the source, you need to use the c-style for

See Effective Go (see references at the end) for an excellent reference on Idiomatic Go

## 33 - Start with simplicity

A core principle of Go is “keep it simple”

As well as purely in code, this principle applies across the language in several key areas

**Frameworks and libraries**

In other languages, there is a tendency to in some ways choose a framework, and then decide a project.

In Go, the philosophy is reversed - only reach for the framework (or an external library) when you need it

The core of Go is very powerful (for example containing a production ready web server) which means in many cases you can build your whole project successfully without straying outside of the core libraries

Where you do need more focused power, the libraries and frameworks that are available usually work as direct- or minimal effort drop in replacements.

**Packages**

As was mentioned earlier, start with the simplest structure and build out - don’t attempt to plan your whole structure from the start (you’ll spend more time planning than coding!)

**Concurrency**

This is a biggie! Many people do is assume you need to use goroutines and channels everywhere

In reality, you should only reach for a Go routine when you need one.
For example, the built in web server is concurrent by design.

With great power comes great responsibility! Go’s goroutines and channels are very powerful but using them can very quickly ramp up the complexity when you don’t need it.

## 34 - Any final thoughts?

A few general things before we’re done!

Despite Go being created by a search engine company, it has an awful name to search for! If you want to find something, search “golang” instead of “go”

Go has an opinionated formater with one style - use it! Most IDE plugins will allow you to run it on save by default

If you’re finding yourself spending too long designing your code, consider you may be overthinking it! Start simple and add complexity as required.

## 35 - Any questions?

Any questions?

## 36 - About me

Thanks for listening!

You can find me on twitter and github (where I’ll be publishing these slides and some handy references), and for totally unrelated artwork I’m also on instagram - I promise no selfies!

## 37 - See also

_none_
