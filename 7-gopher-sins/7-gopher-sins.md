# 7 Deadly Gopher Sins

> This document contains a summary of the speaker notes used to present this talk to accompany the [pdf snapshot of the slides](7-gopher-sins.pdf).
> 
> These notes can be a little abstract and more aide-memoirs to the speech giver, and are not intended to be read as prose, so forgive the fragmented sentences!

- [7 Deadly Gopher Sins](#7-deadly-gopher-sins)
  - [1 - Title page](#1---title-page)
  - [2 - Who am I?](#2---who-am-i)
  - [3 - **1. Lust**](#3---1-lust)
    - [4-5 - The sales pitch](#4-5---the-sales-pitch)
    - [6-7 - Adding complexity](#6-7---adding-complexity)
    - [8 - How to avoid Lust](#8---how-to-avoid-lust)
  - [9 - **2. Wrath**](#9---2-wrath)
    - [10-11 - Using Must](#10-11---using-must)
    - [12 - How to avoid Wrath](#12---how-to-avoid-wrath)
  - [13 - **3. Greed**](#13---3-greed)
    - [14 - But what about](#14---but-what-about)
    - [15 - How to avoid Greed](#15---how-to-avoid-greed)
  - [16 - **4. Sloth**](#16---4-sloth)
    - [17-19 Comments](#17-19-comments)
    - [20-21 Error context](#20-21-error-context)
    - [22 - How to avoid Sloth](#22---how-to-avoid-sloth)
  - [23 - **5. Gluttony**](#23---5-gluttony)
    - [24 - Frameworks](#24---frameworks)
    - [25 - How to avoid Gluttony](#25---how-to-avoid-gluttony)
  - [26 - **6. Envy**](#26---6-envy)
    - [27 - Compare Python and Go](#27---compare-python-and-go)
    - [28 - How to avoid Envy](#28---how-to-avoid-envy)
  - [29 - **7. Pride**](#29---7-pride)
    - [30-31 - Examples and plugs](#30-31---examples-and-plugs)
    - [32 - How to avoid Pride](#32---how-to-avoid-pride)
  - [33-35 - **Bonus sin**](#33-35---bonus-sin)
  - [36 - Thankyou and social links](#36---thankyou-and-social-links)
  - [37 - References](#37---references)

## 1 - Title page

Hi and welcome to my talk.

Today I’m going to be taking you through what I feel are 7 of deadliest sins in Go.

These are mostly very much things I myself have been guilty of or experienced at least once in my career, so hopefully this may save you some of that pain!

Some of these are going to come with examples, some are going to be more my relating experiences, but they all come with gophers!

## 2 - Who am I?

To begin at the beginning, who am I?

I’m John

Some of you may have seen my talk at Gophercon UK last year and I’m honoured to have been asked back again!

Currently I’m a senior engineer using Go at Admiral Money.

I’m also an artist, dabble in circus and fire skills, and ich spreche auch ein bisschen Deutsch!

So without further preamble, let’s get started and because we all love Go

## 3 - **1. Lust**

…let’s start with Lust.

But I’m not talking about love here, so… what?

Let me take you back for a moment to when we were kids.
We’ve all felt it - toy with action features rush to play - arm comes off

Go is that toy - want some of that

Ok in hobby project, but Go is sold as really easy to use, so they rush to build them into production solutions.

But why problem?

Tempt to Go - features - goroutines

Start with how they’re sold

### 4-5 - The sales pitch

Well, I’m sure you’ve probably all seen the “sales pitch” which is very like that toy advert on TV.

“...BOOM! Goroutines!”

Except… that’s not really true.

I mean it’s technically correct (you know, the best kind of correct), but it’s not the whole story.

Anyone that’s done anything with goroutines and probably tell me straight away what’s wrong with this code (audience question)...?

More than just the keyword.

### 6-7 - Adding complexity

Start with a straightforward function to convert then sum some numbers.

Then think - but we should be using goroutines!

Once we introduce goroutines however, the code is twice as long and we suddenly have a whole new set of considerations:

- Can’t just stick go in front of our string conversion.
- Can’t just increment our sum directly anymore as multiple goroutines can’t safely write to the same variable.
- Can’t just return an error as we did before as when you add the go keyword it doesn’t allow return values. So we need another channel (or errgroups or similar)
- And finally we need to wait for the goroutines to do their work and receive the results.

### 8 - How to avoid Lust

_no notes_

## 9 - **2. Wrath**

So from lust to wrath

Who remembers Hitchhiker’s  - Don’t panic!

By which I’m referring to runtime crashes, not running around screaming!

But by Don’t Panic I’m not saying it’s a sin to not write perfect code, because out of control…

Firstly relying on panics as an error handling strategy, treating them as exceptions.

Analogy (see slide)

Both scenarios achieve the desired outcome of stopping the car.

But real sin is intentional panic

### 10-11 - Using Must

But as I said, the sin here is about intentional panics.
And now we must talk quickly about must as this is a very common sin.

You see, in Go, by convention a function that is prefixed with Must will panic if it errors - nothing enforces this btw, it’s just convention.

If there is a must, then there will generally always be a vanilla version of the function without the prefix that returns a normal error.

A common example of this, and one I’ve seen sinfully abused a lot, is in the regexp package.

In the first example we’ve dropped a Must into runtime code - this is bad.

For one, it’s inefficient as if the regex doesn’t change, you’re compiling it every request.
And more importantly, if you’ve done something wrong and it panics you’ve broken your users’ journey
If you really need to compile at runtime, check the error properly so you can return something sensible to your user.

But in most cases you probably only need to compile your regex once - so pull it to the package level and use the must to ensure that if it fails to compile it’ll fail fast at startup rather than when serving your users!

### 12 - How to avoid Wrath

_no notes_

## 13 - **3. Greed**

How can we be greedy?
They say you can’t be too prepared. But is that really true?

None of us can see the future.
Some reason in coding we have a habit of attempting to do just that.

Knowing that you’re working on a feature this sprint, and knowing that in the backlog for next sprint another feature is coming up is one thing. 

The sin is to pre-emptively over-engineer and genericise to greedily add functionality to solve problems that not only do you not have yet - you may actually never have.

But why’s that a problem? What’s wrong with future proofing and writing flexible code?

(explain hello world)

### 14 - But what about

Maybe we should … (from the slide)

…and very quickly we suddenly have a behemoth of a service!

Why is this bad?

Now 30 second change is a 6 month rebuild.

### 15 - How to avoid Greed

_no notes_

## 16 - **4. Sloth**

So after all that over engineering, it’s time to slow down with some sloth

You’ve probably heard how laziness can be a virtue, but how so?

And how does working harder allow us to be virtuously lazy?

Well it’s about putting in more thought upfront to reduce cognitive overhead later - whilst  of course still avoiding our previous sin!

Well, let’s start with comments.

### 17-19 Comments

What we don’t want is this - What I wanted was this.

### 20-21 Error context

The other area where context is often skimped on is errors, and this I think is an unfortunate side effect of the if err != nil { return err } idiom.

The intent of forcing you to check errors is ostensibly to encourage you to take action as close to where it occurred as possible.
As touched on in wrath this avoids the need to wade through stack traces etc, and is more efficient in ensuring we don’t waste time and resources on processing anything else if we already know we’ve failed.

But many times, what you will actually see is a whole chain of if err != nil {return err}, which in effect simply bubbles the original error up several layers, by which time the context is lost.

Better to where possibly if you can’t definitely handle an error at site, add context.

### 22 - How to avoid Sloth

_no notes_

## 23 - **5. Gluttony**

So what is our sin of gluttony?

Well, you know when you go on holiday, and when you get there you realise you’ve packed way too much?

Not only
-	are your cases heavy and hard to lift;
-	it’s hard to find anything in your cases without unpacking the whole thing;
-	but you probably don’t need half of it anyway.

Standard “holiday stuff”

Well the same is true of libraries and frameworks in Go.

Just like those things you pack - they can be really useful for the right situation - but if you don’t need them, they’re just extra baggage.

So the sin here isn’t using them when you need them, it’s using them just because.

And why do we do this?

Again, just like the packing scenario, a lot of it is habit. Especially if we have a background in other languages where third party frameworks etc are more prevalent.

### 24 - Frameworks

But why is it a problem?

Every dependency:
- Can go away
- Can have a vulnerability
- Can possibly lock you into an opinionated path you have to spend effort working around.

### 25 - How to avoid Gluttony

_no notes_

## 26 - **6. Envy**

And so to envy

Well this is probably one of the commonest gopher sins I’ve seen, usually in engineers coming from other languages - and I know when I first used Go it was the one I was most guilty of myself!

Essentially it’s the tendency to write Go as if it were another language.

Why is this a sin though?

I mean, as long as it compiles and runs without error, what’s the issue?


Though ultimately it’s usually a recipe for making your code more complex and less maintainable than it needs to be. To return to our sin of sloth and greed, this a good example of doing something you think is for the best, but in the end just makes your life harder.

But what are some examples of this?

### 27 - Compare Python and Go

Let’s open with some straight forward logic flow.

I’m sure we’re all used to nested code like we see on the left, and it’s very much how I coded back when I was using Python.

But as we can see from the code on the right, we can, we a few simple tweaks, make it much cleaner and easier to understand.

It’s down to 14 lines instead of the original 15 - and that includes some added whitespace for readability!

By inverting some of the logic - ostensibly checking the negative path first - we eliminate the need for the nesting and keep the flow clearly in line of sight.

### 28 - How to avoid Envy

_no notes_

## 29 - **7. Pride**

And then we get to pride.

But I’m not saying taking pride in your code is a sin!

The gopher sin here is where you assume you know what’s best for others.

How so?

Well, have you ever been looking for a library to do something, because of course applying the virtuous interpretation of laziness, you don’t want to have to write it yourself if someone else has already done it, but despite finding some, none of them quite work the way you need?

That’s not saying those libraries are bad - they may be incredibly good at what they do - but they’re overly opinionated in a way that was perfect for the author but doesn’t work for you.

_Example of entropy checking function_

### 30-31 - Examples and plugs

_no notes_

### 32 - How to avoid Pride

_no notes_

## 33-35 - **Bonus sin**

Sin of complexity pulling it all together.

## 36 - Thankyou and social links 

_no notes_

## 37 - References

[Slide not presented - included for referencing and attributions]