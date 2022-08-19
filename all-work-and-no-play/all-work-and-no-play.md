# All Work And No Play Makes Gophers... Something Something...

> This document contains a summary of the speaker notes used to present this talk to accompany the [pdf snapshot of the slides](all-work-and-no-play.pdf).
> It does not attempt to be a word-for-word transcript of delivery.

- [All Work And No Play Makes Gophers... Something Something...](#all-work-and-no-play-makes-gophers-something-something)
  - [1 - Title page](#1---title-page)
  - [2 - Who am I?](#2---who-am-i)
  - [3 - Intro](#3---intro)
  - [4 - Coming up](#4---coming-up)
  - [5 - 1 Title Card - Getting here](#5---1-title-card---getting-here)
  - [6 - 1.1 Humble beginnings](#6---11-humble-beginnings)
  - [7 - 1.2 First steps](#7---12-first-steps)
  - [8 - 1.3 Some classic games](#8---13-some-classic-games)
  - [9 - 1.4 Doing a lot with a little](#9---14-doing-a-lot-with-a-little)
  - [10 - 1.5 Inspiration: Phantom Slayer](#10---15-inspiration-phantom-slayer)
  - [11 - 2 Title Card - Designing the game](#11---2-title-card---designing-the-game)
  - [12 - 2.1 Where to start?](#12---21-where-to-start)
  - [13 - 2.2 Goals and Constraints](#13---22-goals-and-constraints)
  - [14 - 3 Title Card - Building the game](#14---3-title-card---building-the-game)
  - [15 - 3.1 Sub Title - The Maze](#15---31-sub-title---the-maze)
  - [16 - 3.1.1 Get on the grid](#16---311-get-on-the-grid)
  - [17 - 3.1.2 Getting to the point](#17---312-getting-to-the-point)
  - [18 - 3.1.3 A-mazing!](#18---313-a-mazing)
  - [19 - 3.2 Sub Title - The Player](#19---32-sub-title---the-player)
  - [20 - 3.2.1 In a bit of a state](#20---321-in-a-bit-of-a-state)
  - [21 - 3.2.2 Move it](#21---322-move-it)
  - [22 - 3.2.3 There and back](#22---323-there-and-back)
  - [23 - 3.2.4 Round and About](#23---324-round-and-about)
  - [24 - 3.3 Sub Title - The View](#24---33-sub-title---the-view)
  - [25 - 3.3.1 Start simple](#25---331-start-simple)
  - [26 - 3.3.2 Box it up](#26---332-box-it-up)
  - [27 - 3.3.3 Slice and Dice](#27---333-slice-and-dice)
  - [28 - 3.3.4 Pixel Perfect](#28---334-pixel-perfect)
  - [29 - 3.3.5 ASCII Anything](#29---335-ascii-anything)
  - [30 - 3.3.6 Look out](#30---336-look-out)
  - [31 - 3.3.7 Dealing with different architectures](#31---337-dealing-with-different-architectures)
  - [32 - 4 Title Card - Conclusions](#32---4-title-card---conclusions)
  - [33 - Have fun!](#33---have-fun)
  - [34 - Any Questions?](#34---any-questions)
  - [35 - Thanks!](#35---thanks)
  - [36 - Credits](#36---credits)
  - [37 - References](#37---references)

## 1 - Title page

Hello and welcome

## 2 - Who am I?

My name's John

Currently Senior Engineer using Go at Admiral Money

I'm also an artist, dabble in circus skills and sometimes spin some fire

## 3 - Intro

Today I'm going to be talking to you about a retro inspired game I wrote in Go called 3D Gopher Maze

All the code for the game can be found on my github

## 4 - Coming up

I'll start off with some history and inspiration for the game

Then run through some design decisions and constraints

Then look at building the actual game

## 5 - 1 Title Card - Getting here

So, to begin with, a little nostalgia

## 6 - 1.1 Humble beginnings

Going back to the beginning, my first computer was my brother's **Dragon 32**

_Reading from bullets on slide_

Unlike the family in the photo, we only had a black and white portable TV

## 7 - 1.2 First steps

The Dragon came with a BASIC interpreter

My first ever program was very likely this one (_explain code_)

Wasn't Earth shattering, but it was fun!

## 8 - 1.3 Some classic games

The **Dragon** had a lot of classic games

- Some originals
- Some from other platforms
- Some legally dodgy ones (_explain **Donkey King**_)

All had one thing in common (_lead to next slide_)

## 9 - 1.4 Doing a lot with a little

Dragon didn't have a lot of resources

Developers had to use some clever tricks to write games

Why not try to write a retro inspired game?

## 10 - 1.5 Inspiration: Phantom Slayer

One of my favourite games on the **Dragon** was _Phantom Slayer_

_Read from slide_

Object of the game to run around the maze shooting or avoiding the Phantoms for as long as possible.

Watching TV and thought of the game

How to solve the issue of displaying a pseudo 3D view?

## 11 - 2 Title Card - Designing the game

So now let's get on with designing the game

## 12 - 2.1 Where to start?

How to write a game?

Loads of options, just as in any software.

Like a talk, so much to put in it's hard to finish - or even to get started

So needed to start with some goals and constraints to reduce the problem space

## 13 - 2.2 Goals and Constraints

(_explain through slide_)

## 14 - 3 Title Card - Building the game

Ok, so now I knew what I wanted to build, it was time to get on with building it!

## 15 - 3.1 Sub Title - The Maze

The core thing in a maze game is a maze!

## 16 - 3.1.1 Get on the grid

- Decided to base on a grid
- Like a chess board
- Can take step forward or back, or rotate 90degrees left or right
- Zero indexed top left

Can see the grid with dark squares for walls, light for passages and special **p** and **g** (_explain start points_)

Representing the maze as a 2D array (slices) (_explain definition_)

## 17 - 3.1.2 Getting to the point

When the game starts up it imports the chosen maze map into a Maze struct (_look at next slide_)

In addition it also stores the set of panels to be used later in the view.

This is an incomplete feature - as the longer term intention was to allow different display panels to be swapped in, for example to have a larger or smaller view window.
But will get onto the UI in a few slides time!

Once we have this maze, we can access any space within it using a handy `getSpace` helper.

## 18 - 3.1.3 A-mazing!

So, to look at the import that happens when the game starts

We loop through the maze definition (the 2D array), first by row, then column with nested range

For each space in the grid we check the type - if it’s a gopher or player start, we store those points into slices - then store the space type into the grid.

Where we found a gopher or player, we assume the underlying space type is an empty one!

The gopher gets special status as an item for the player to find or collect.

The maze is now ready!

## 19 - 3.2 Sub Title - The Player

There’s no point having a maze though, if there’s no one to run around it!

So we need next to define the player.

## 20 - 3.2.1 In a bit of a state

The player is actually super simple!

All we need to know is our current state: where we are, and which way we’re facing!

A struct is a perfect way to represent this in a couple of simple fields:

The position, p, representing an x,y coordinate in our maze grid
The orientation, o, representing a cardinal direction:, n for north, s for south etc

And that’s pretty much it.

But the player isn’t much good if they can’t move.

(_mention single letter var names_)

## 21 - 3.2.2 Move it

As we’re based on a grid, moving is just a matter of applying a move vector to our current position to get our new position.

The vector to apply depends on the direction we’re facing as we see here

So for example … (speak through scenarios)


## 22 - 3.2.3 There and back

Taking a look at the code, we can see how we apply the vector to the player’s position.

The vector we are going to want to apply is stored in the game state based on the player’s direction
See this in the next slide when we look at turning

When we want to move backwards, we do the same thing as moving forwards, except we multiply the vector by -1 so we move the opposite way.

In either case, we don’t want the player to end up inside a wall, so before we actually move, we perform a ghost move to check the proposed destination

The isMoveToWall function retrieves the proposed space from the current map and returns true if it’s a wall.

In addition, when we move forward we also check whether the Gopher is in the square ahead of us - if it is we’ve won the game!

The Is function here is a receiver function on a Point type, that checks whether the given points are the same point.

## 23 - 3.2.4 Round and About

Rotating is also fairly straightforward as we know we’re turning in 90 degree increments to follow the grid

That means each right turn is 90 degrees clockwise, and left is 90 degrees anticlockwise.

Each time we want the player to rotate, then we take note of our current orientation and shift to the next one in the rotation.

So, if we’re already facing North and want to turn right, our new orientation gets set to East and we update the move vector to move us in that direction if we then choose to move forward.

## 24 - 3.3 Sub Title - The View

Now that we can move around, we need the player to know where they’re going.

Possible to play a maze game completely through just a text interface like an old adventure game like Zork etc

Describe where you are, what you can see, and any exits

But this was going to be a 3D adventure game, so I needed a way to show the player where they were going.

Designing the view was the biggest challenge of writing the game, so I’ll break it down step by step.

## 25 - 3.3.1 Start simple

So, first consider a simple corridor with a gopher standing in it

It’s a short corridor with a dead end up ahead and a side passage

On the right, we can see the view that the gopher would be able to see

We can see the :

A little to the left and right of where we’re standing
The side passage just ahead and to the right
The deadend straight ahead

(_explain alternating wall colours_)

## 26 - 3.3.2 Box it up

Now, let’s look a bit closer at how the projected view relates to the map

We can do this by overlaying a set of red boxes on both views

This shows us the 4 grid squares that we can see - 3 ahead, one to the side

Not looking behind us!

This is a clue to how to display the view - each grid square is represented by a concentric square ring (getting smaller - apart from the outer!)

Don’t care about floor and ceiling

## 27 - 3.3.3 Slice and Dice

So can split into a set of vertical columns

This allows rendering any view in the maze with a small set of standard panels (13 here - could be optimised)

Each slice gets smaller as it gets towards the center (perspective!) - though notice the outer two are the same size - this is because half of the square is to your side, so the view is pushed slightly further forward!

## 28 - 3.3.4 Pixel Perfect

Of course, I wanted to run this game in the terminal, without using any kind of canvas for more traditional drawing.

What a terminal does have though, is rows and columns for text.

Very much like a grid of actual pixels on the screen.

So can use each character as a pseudo pixel in an 11 x 9 grid (played around with the numbers to get a good aspect ratio)

Each of the two outer slices are 2 pixels wide, and the middle three 1 - this is to simulate the perspective coming to a point as best as possible with limited resolution.

But how to actually draw the pixels on the terminal?

## 29 - 3.3.5 ASCII Anything

To get simple images on screen, games on the Dragon often used text characters, and had a few special ones specifically for this reason.

It turns out in a similar way, that if you delve into the further reaches of the ASCII character set, you can find a whole set of helpful characters that can be used for the same purpose..

I found a couple of characters that are essentially single colour greyscale blocks, and these were ideal.

Could use these to render the bi-coloured walls, and use a simple mod function to alternate them as the player turned.

In addition, there are some nice “frame” characters that I used to make the outline of the game window a bit nicer!

And this is what the view ends up looking like for the corridor we were looking at before.

Compile set of panels, then read each row. (next slide is which spaces to build)

## 30 - 3.3.6 Look out

How to decide what to render?

Don’t want to try to render the whole map

Wall culling

## 31 - 3.3.7 Dealing with different architectures

Keeping things simple in terms of the terminal

Didn’t want to use any external libraries - solve the problem simply myself!

Simply clearing the screen and redrawing each “frame”

However, different OSes have different commands

Using build tags to have two different versions of the same command.

(_explain the //+build and the `_windows_amd64` postfixes_)

## 32 - 4 Title Card - Conclusions

So what was the point of this?

## 33 - Have fun!

Don't always have to build the **Next Big Thing**(tm)

## 34 - Any Questions?

## 35 - Thanks!

Close up

**END OF PRESENTATION**

## 36 - Credits

## 37 - References
