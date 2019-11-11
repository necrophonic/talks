# Zero to Gopher - Speaker Notes

> This document contains a summary of the speaker notes used to present this talk to accompany the [pdf snapshot of the slides](zero-to-gopher.pdf)

- [Zero to Gopher - Speaker Notes](#zero-to-gopher---speaker-notes)
  - [1 - Title page](#1---title-page)
  - [2 - Contents](#2---contents)
  - [3 - History and overview](#3---history-and-overview)
  - [4 - Rob Pike quote](#4---rob-pike-quote)
  - [5 - Language Tour Header](#5---language-tour-header)
  - [6 - 25 Keywords](#6---25-keywords)
  - [7 - 19 Basic Types](#7---19-basic-types)
  - [8 - 6 Composite Types & 3 Containers](#8---6-composite-types--3-containers)
  - [9 - Cool Stuff Header](#9---cool-stuff-header)
  - [10 - No semicolons](#10---no-semicolons)
  - [11 - Privacy by convention](#11---privacy-by-convention)
  - [12 - Cross compilation](#12---cross-compilation)
  - [13 - Errors, not exceptions](#13---errors-not-exceptions)
  - [14 - Static, not noisy](#14---static-not-noisy)
  - [15 - Compiler on your side](#15---compiler-on-your-side)
  - [16 - Only one loop](#16---only-one-loop)
  - [17 - Ensure things with defer](#17---ensure-things-with-defer)
  - [18 - One format](#18---one-format)
  - [19 - One of Go’s main strengths](#19---one-of-gos-main-strengths)
  - [20 - Concurrent by design](#20---concurrent-by-design)
  - [21 - Slices](#21---slices)
  - [22 - FAQ Header](#22---faq-header)
  - [23 - FAQ: Is Go object oriented](#23---faq-is-go-object-oriented)
  - [24 - FAQ: Why doesn't Go have generics](#24---faq-why-doesnt-go-have-generics)
  - [25 - FAQ: Should I use Go for everything](#25---faq-should-i-use-go-for-everything)
  - [26 - Cardiff Go](#26---cardiff-go)
  - [27 - Thank you & About me](#27---thank-you--about-me)
  - [28 Any Questions](#28-any-questions)

## 1 - Title page

Hi and welcome to my talk

> General "about me"

I’ve been using Go, mostly for personal projects, for a few years now and am currently leading a wave of interest in Go at the office

This talk today is going to be a quick introduction to the world of Go

Half hour isn’t enough to cover everything in depth - most features could easily fill a whole workshop on their own!

But I intend to give you a flavour of what Go is, some of its key features and hopefully answer some of your questions!

## 2 - Contents

I’ll start with some history

Then a lightning tour through the core syntax of the language

Then we’ll get to the cool stuff - the features that make Go an awesome language

Lastly I’ll cover some frequently asked questions about Go

Then there’ll (hopefully!) be time for some questions (although you can catch me afterwards during the day!)

## 3 - History and overview

So, where did we begin?

## 4 - Rob Pike quote

Go was developed at Google in 2007 to improve developer productivity and address criticism of other languages that were in use at Google at the time, whilst maintaining their strengths

For example

- c/c++ : Static typing and runtime efficiency are good, but compile times can be long and memory management is hard amongst others
- python : Very readable and usable, but at the sacrifice of performance

As shown in this quote from Rob Pike (READ)

The idea being to maximise developer experience and generally get out of your way; letting you get on with solving the actual task at hand.

## 5 - Language Tour Header

So without further ado, I’ll start with a lightning tour through the core syntax of the language

Not going to go in depth - plenty of fantastic resources out there that’ll teach you the ins and outs in detail (some of which I’ll link later) - but will give you a flavour of the shape of the language.

## 6 - 25 Keywords

The core language itself consists of only 25 keywords

Some are similar to those found in other languages
Some are special to Go

Go designed to be as concise and unambiguous as possible to improve developer experience

They fall broadly into 4 categories:

- Declare code elements - `const, func, import, package, type, var`
- Declare composite types - `chan, interface, map,  struct`
- Control flow - `break, case, continue, default, else, fallthrough, for, goto, if, range, return, select`, `switch`
- Special control flow - `defer`, `go` are also control flow keywords, but modify function calls in special ways _(see later)_

## 7 - 19 Basic Types

Go is a statically typed language and has 19 basic types

Most may be familiar to you from other languages

- strings
- booleans
- numbers (several flavours: int, float and complex) etc

And one you won’t have seen before, the _rune_

Go is a unicode aware language and the rune type is used to natively deal with unicode code points

## 8 - 6 Composite Types & 3 Containers

- Pointers and structs are similar to their C equivalents
- Functions are first class types in Go and can be passed around like other types
- Channels are used to synchronise data between Goroutines (coming later!)
- Interfaces - collection of method signatures an object can implement - unlike other languages, Go’s are implemented implicitly rather than explicitly - You’ll never see an implements keyword!
- Containers

Containers have 3 subtypes

- Arrays are as you may expect
- Maps are associative arrays (hashtables) in Go - similar to for example a Dict in python. **Note**, _The name sometimes gets confused for "mapping functions"_
- Slices are a special kind of array special to Go and you’ll generally see them more in the wild than “classic” arrays - but more on them soon!

## 9 - Cool Stuff Header

.. and now onto the cool stuff!

Quick note that in most examples I’ve omitted some of the basic furniture such as package definitions for brevity

With that said, in no particular order, let’s dive in!

## 10 - No semicolons

Starting with a simple, but I think, still cool one!

No semicolons! (well mostly!)

This leads to:

- Cleaner code - literally less cluttering your screen
- Fewer silly bugs - no more weird syntax issues that are actually down to a simple missing semicolon - we’ve all had “error on line XX” errors that turned out to be a semi-colon you missed about 200 lines back.

In fact the only place you are likely to see them in Go is in for loops (SEE EXAMPLE)

(BONUS)

Actually there are semi-colons in Go - it’s just that the compiler inserts them for you. One less thing to remember!

## 11 - Privacy by convention

Public/private accessibility in Go is purely by convention

This is a cool one that plays to Go’s drive to simplicity

If a package variable, type or function begins with an upper case letter, it’s visible to your entire program.

If it starts with a lowercase letter, it’s only visible within its own package.

That’s it!

## 12 - Cross compilation

With other traditional compiled languages, you need to compile code on the platform you want the binary to run on.

With Go, you can build for any supported platform from wherever you write your code - simply with compiler flags passed to `build`

This means you can build on a macbook and get a binary to run on ubuntu, windows or even a raspberry pi amongst others!

## 13 - Errors, not exceptions

Go may be exceptional, but it’s errors aren’t - in a good way!

Most functions in Go, as well as potentially returning a set of data, also usually return an `error` type - that is, a value that satisifies the `error interface`

The idiomatic way to work with these is to check them immediately and take action at the site of the error. This leads to cleaner, more obvious code then long try… catch blocks where break of execution is not necessarily easy to follow.

It also means no more “unhandled exceptions”!

The if `err != nil` pattern is one you’ll see a lot in Go.

- Divisive - some people don’t like the pattern as they feel it’s overly verbose. However a core tenet of Go is that code is clear and explicit about what it’s doing - no magic here!

## 14 - Static, not noisy

Go is `statically typed`, but it’s not `noisily typed`

What do I mean by that?

In a regular typed language you would normally have to always explicitly tell the compiler the type you want
Can be a bit tedious when most of your vars are basic types

Using the := (also known as “hippo”) operator, you can declare and assign a variable for common types in a single statement

The variable will take the default basic type for each case

(REFER TO CODE)

## 15 - Compiler on your side

The Go compiler really is on your side!

Above is a trivial example (a variable declared and not used), but the compiler will catch a variety of things like this that strongly indicate you may have a bug in your code.

Instead of letting you continue and spend ages wondering why the value you think you set isn’t working, the compiler will stop you before you start!

- Reduces bugs
- Cleaner code - only contains things that are actually relevant

## 16 - Only one loop

There is only one looping construct in Go - for

Other loop behaviors can be implemented by omitted the statements

- Classic for - is a c style for loop with initialiser, exit condition and iterator
- While loop - is implemented by omitting the initialiser and iterator
- An infinite loop - omits all the statements
- Range loop - to iterate over arrays, slices and maps - unicode strings range natively over the code points

## 17 - Ensure things with defer

Always forgetting to close resources? Let defer() do it for you!

Similar to a finalise, defer ensures the given function will execute when it falls out of scope.

In the above, once we know the new file has been created correctly, we defer closing it and let Go take care of it.

The code is a simple case, but imagine having lots of logic and possible returns in the function. defer ensures, outside of a panic that the file will always be closed without us needing to remember to do it everywhere.

This leads to cleaner and safer code

## 18 - One format

The Go toolchain includes the fmt command - a built in, opinionated formatter.

This means Go code is:

- easier to write: never worry about minor formatting concerns while hacking away,
- easier to read: when all code looks the same you need not mentally convert others' formatting style into something you can understand.
- easier to maintain: mechanical changes to the source don't cause unrelated changes to the file's formatting; diffs show only the real changes.
- uncontroversial: never have a debate about spacing or brace position ever again!

## 19 - One of Go’s main strengths

Concurrency is a core component of Go rather than a bolt on

Implemented with goroutines

- green threads - scheduled by the runtime rather than the underlying OS
- lightweight - the runtime can run 1000s of goroutines at once for very little cost (compared to say, java threads)

(REFER TO EXAMPLE)
In the code shown, the first example runs sequentially.
The second runs concurrently - just with the addition of the go

## 20 - Concurrent by design

Now you have things running concurrently, you need to be able to return data

In most other languages this needs to be carefully coordinated to avoid race conditions writing to memory

In go, we use channels

Simple queues - can be one-in-one-out or buffered as needed

(REFER TO EXAMPLE)

Here we make a simple channel of type int (remember, Go is strongly typed so everything needs a type! - but this could just as easily be struct or func!)

The channel is passed to the function as a normal argument

The function then just writes it’s result to the channel

The `result := < -c` declares an integer variable (inferred from the channel!) and blocks waiting for a value on the channel.

Once received the value is assigned to result and the program continues

----

(BONUS)

Go does have mutexes under the hood (and you can use them directly if you do need), but in the most part, Go does the hard work for you!

## 21 - Slices

This is certainly a subject that could fill an hour on its own! As with other topics I’ve linked some good resources at the end.

Arrays by design are fixed length data structures.

If you want to manipulate them you either end up with sparsity when you remove stuff, or gratuitous memory allocation and manipulation when you need to elongate or splice them.

With a variety of supported standard operations, slices make it all much easier!

Slices are declared using the make keyword and take a type, length, and optionally capacity

A good way to think about a slice is a as a variable length window than can move and change views in a lightweight fashion over an underlying concrete array

(BONUS)

Under the hood, there are concrete arrays. It’s just that you’re letting Go manage them more efficiently and flexibly.

## 22 - FAQ Header

Before we finish, I’ll touch on some of the commonly asked questions about Go (and some of the criticisms!)

## 23 - FAQ: Is Go object oriented

Quite a common question! And yes, the answer is yes and no

Structs are similar to objects in that they can be assigned attributes and behaviour

However

There is no type hierarchy or inheritance - inheritance as it exist in Go is via composition.

This means you can embed structs inside other structs. More to get into now, but this is an extremely powerful construct and much simpler and safer than classic inheritance can be

Also, by convention Go does not use getters and setters - you access public fields directly.

Not saying you can’t have getters/setters, but it’s not usual to do so

## 24 - FAQ: Why doesn't Go have generics

Mostly to reduce complexity - both of the internals and for developer comprehension.

Having generics makes code arguably less clear as to what something may do and makes catching errors harder

That said, they’re not bad things - and if you genuinely have a need for generics, then absolutely use a language that has them.

Which leads on to … (NEXT SLIDE)

## 25 - FAQ: Should I use Go for everything

Mostly to reduce complexity - both of the internals and for developer comprehension.

Having generics makes code arguably less clear as to what something may do and makes catching errors harder

That said, they’re not bad things - and if you genuinely have a need for generics, then absolutely use a language that has them.

Which leads on to … (NEXT SLIDE)

## 26 - Cardiff Go

Just a quick word about Cardiff Go

- Started around 4 years ago by Eleanor Deal
- Usually meet the first Thursday in every month for talks, workshops and socials
- Come along and see us! (we have dragon stickers!)

## 27 - Thank you & About me

Thanks for listening!

You can find me on twitter and github (where I’ll be publishing these slides and some handy references), and for totally unrelated artwork I’m also on instagram - I promise no selfies!

I’ll be publishing these slides and references later and they’ll be available via my twitter and devfest

I’ll be available throughout the day so feel free to come say hi if there’s anything you’d like to ask

And saying that (NEXT SLIDE)

## 28 Any Questions

> no notes
