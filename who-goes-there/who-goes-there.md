# Who Goes There - Speaker notes

> This document contains a summary of the speaker notes used to present this talk to accompany the [pdf snapshot of the slides](who-goes-there.pdf)

- [Who Goes There - Speaker notes](#who-goes-there---speaker-notes)
  - [1 - Title page](#1---title-page)
  - [2 - Who am I?](#2---who-am-i)
  - [3 - Coming up](#3---coming-up)
  - [4 - History](#4---history)
  - [5 - ONS](#5---ons)
  - [6 - Revisiong Control](#6---revisiong-control)
  - [7 - Open Source](#7---open-source)
  - [8 - Expansion](#8---expansion)
  - [9 - Inspiration: gu-who](#9---inspiration-gu-who)
  - [10 - Using Go](#10---using-go)
  - [11 - Tech intro card](#11---tech-intro-card)
  - [12 - Technologies](#12---technologies)
  - [13 - Why Lambda](#13---why-lambda)
  - [14 - Aside: Lambda Destinations](#14---aside-lambda-destinations)
  - [15 - Why Serverless](#15---why-serverless)
  - [16 - Why GraphQL](#16---why-graphql)
  - [17 - Aside: GraphQL vs REST](#17---aside-graphql-vs-rest)
  - [18 - Why Event Driven](#18---why-event-driven)
  - [19 - Bringing it together title card](#19---bringing-it-together-title-card)
  - [20 - High level flow](#20---high-level-flow)
  - [21 - Code Dive title card](#21---code-dive-title-card)
  - [22 - Repository layout](#22---repository-layout)
  - [23 - The Checker Lambda](#23---the-checker-lambda)
  - [24 - Structure](#24---structure)
  - [25 - Env vars](#25---env-vars)
  - [26 - Query](#26---query)
  - [27 - Return](#27---return)
  - [28 - The GraphQL Query](#28---the-graphql-query)
  - [29 - GraphQL module](#29---graphql-module)
  - [30 - The actual query](#30---the-actual-query)
  - [31 - The Slack Notifier lambda](#31---the-slack-notifier-lambda)
  - [32 - Notifier structure](#32---notifier-structure)
  - [33 - The blocks API](#33---the-blocks-api)
  - [34 - The output](#34---the-output)
  - [35 - Demo](#35---demo)
  - [36 - Thankyou page](#36---thankyou-page)
  - [37 - References and attributions](#37---references-and-attributions)

## 1 - Title page

Hi and welcome

## 2 - Who am I?

My name’s John

Working in software and tech, in public and private sectors, since 2000, 

Using Go personally and professionally since around 2016

Currently working as a senior software engineer for Admiral Financial Services and helping lead the adoption of Go

Outside of work, despite pandemic, I also co-run the Cardiff Go meet up

## 3 - Coming up

Tool I started developing whilst working at the Office for National Statistics in late 2019

Everything correct to the best of my knowledge when I left!

I’ll start with a little background on the ONS and why I started developing the tool

Then talk through some of the key technologies I chose; what they were; and why

We’ll then look at how these parts come together to form the service, and how you can use similar patterns for your own tools

## 4 - History

So let’s get started with how we got here with a little history

The Office for National Statistics (ONS) was formed on 1 April 1996 by the merger of the Central Statistical Office (CSO) and the Office of Population Censuses and Surveys (OPCS).

## 5 - ONS

You’ve probably heard of the Office for National Statistic in the news when numbers are quoted

from unemployment
to the most popular baby names (which were most recently Oliver and Olivia if you’re wondering!)

They do what it says on the tin - compile national statistics

The were: 

originally founded in 1996 through a merger of older departments

bringing all the older processes and disparate tech stacks (where there was tech!) that entails.

Since then, tech adoption across the organisation has flourished, culminating in this years’ first digital by default UK census.

## 6 - Revisiong Control

Due to its history and reliance on some proprietary tools, ONS originally found itself with a wide range of different source control methods and tools.

Ranging from

literally just copying files to things like
Team Found Server
Mercurial
Subversion
… among others, as well as some vendor specific bespoke solutions.

Don’t need single one-tool-to-rule-them-all, but having a lot of disparate ways of doing the same thing leads to little silos of knowledge and makes team mobility hard.

## 7 - Open Source

The ONS is a public sector organisation - paid for by you

Therefore, transparency about how their statistics are generated as they need to be trusted
(within bounds of confidentiality, sensitivity and data protection of course)

For these reasons it was decided that a cloud based solution would be the way to go

Several of the newer greenfield teams (census) chose and started using Github

## 8 - Expansion

Office for National Statistics github usage*
*Approx. user, team and repository numbers circa start 2020
From those early beginnings around 2015ish with a few small teams, usage grew in a few years

With this naturally came challenges

Newer teams were more used to working in the cloud, with all the security considerations that entails
More legacy teams, through no fault of theirs, weren’t so exposed to new practices

So needed ways to keep good governance and security

This included things such as
the right people having write access to the right repos
and enforcing multifactor authentication

## 9 - Inspiration: gu-who

For awhile, ONS experimented with gu-who from the Guardian

Written in Scala - few in house skills

The version available at the time wasn’t as flexible as the ONS would have liked

Taking gu-who as inspiration, I decided in learning and development time to start building a Go based tool more suitable to being run and supported by the ONS

Using go!
Go was a great fit as it has:

fast start up and execution
simplicity for learning and support
good support across the services I wished to use.

## 10 - Using Go

I chose to write in Go, not only because I’m a massive Gopher! but,

Its speed is highly desirable when you’re paying by execution time
It is relatively straightforward for existing software engineers (and even total beginners) to pick up
More supportable and sustainable

It was well supported across the aws services I was intending to use

## 11 - Tech intro card

But on to the fun bit that you’re really here for - the tech stuff!

## 12 - Technologies

When I started building WGT I came up with some key design features that would enable rapid and simple building of a proof of concept service.

Note:
I primarily chose aws technologies as aws was the primary cloud being used by ONS.
Most major clouds have equivalents that you could swap out for.

Will expand on these in a moment, but:

AWS Lambda for flexibility and cost
Serverless framework for easy repeatable deployment
GraphQL API for simple queries
Event driven architecture for extensibility

## 13 - Why Lambda

So why lambda?

For those unfamiliar, lambda (or a serverless function)

Allows you to execute code without the need to provide any server code or resources

The engine takes care of wrapping with the appropriate runtime and executing the code.

There are many pros and cons to using lambda, but key reasons I chose were:

Cost - only pay for what you use - so for an infrequent runs cost effective. Low runs can fit into free tier.
Triggers - can be triggered by a variety of event sources - so could use a scheduled event, or file in s3
No servers - don’t need to create any servers, or implement server code - no need for http.Server
Destinations - can be configured to automatically post payloads to other services via destinations feature

Go also well supported by lambda and a food fit as mentioned due to its efficiency and speed

## 14 - Aside: Lambda Destinations

A quick aside on destinations

A fairly new feature of aws lambda at the time

Allow definition of targets to be invoked either on_success or on_failure.

AWS takes care of the marshaling of your payload to the appropriate shape, and communicating with target service.

Don’t have to configure both success and failure or indeed either

## 15 - Why Serverless

Replicable Builds - Infrastructure as code is a great way to get reliable and importantly replicable builds.

Would have been a lot harder to do this talk!

Built for serverless - Designed specifically for serverless applications

Cross Cloud Support - Easy to deploy to different clouds

Not without some changes, but reduced effort as to otherwise

Packaging - Can pull whole application up and down with simple commands

Takes care of dependencies
No need to pull together separate systems - such as infrastructure with Terraform then using awscli to update services

## 16 - Why GraphQL

GraphQL is an API language that, as a client, essentially allows you to fetch just what you want

There’s more to it than that, but for my application that was the core reason I chose it.

Some advantages (not full list)

Single API Call - Fetching data in a single API call rather than potentially calling multiple endpoints
No over- or under fetching - REST responses are fixed, but with graphQL you choose which fields you want from the schema
Built in validation and type checking - built in introspection allows validation and automated discovery

In essence, the work of following and aggregating the data is deferred to the server, rather than a responsibility of the client.

## 17 - Aside: GraphQL vs REST

Here’s some other general differences between graphQL and REST

Not an exhaustive list

There are pros and cons ether way, so choose which is better for your application (where they’re both available!)
Note, I’m mostly approaching this as a consumer of graphQL - considerations for running a graphQL server can be different.

## 18 - Why Event Driven

In a nutshell, event driven architecture is based around the producing and consuming events

Events can be anything
could be anything like a user logging in, or a database record has been updated etc.
Makes decoupling services easier - one failure doesn’t necessarily take down your whole application
Enables extensibility as it’s easy to add new producers and consumers

There are many mechanisms for doing this, such as for example aws eventbridge which is specifically built for the purpose.

Here, I chose to use a simple aws sqs queue for quick ease of set up and that it integrated well “out of the box” at the time with lambda destinations.

## 19 - Bringing it together title card

Now we have the foundations, we can bring it all together into the actual service

## 20 - High level flow

The core process is fairly straightforward:

The checker lambda is activated via a cloudwatch event (like a cron job) and calls Github via the GraphQL API
The result of the call is put into a report summary and placed on the event queue using on_success
Clients subscribed to the queue receive the report and perform actions - in the example they format and publish the report to a slack channel

## 21 - Code Dive title card

And now a tour into the actual code

Note:
I’ve paraphrased the code a little in the examples for better slide layout.
The examples here aren’t go fmt’d !
I’ve also omitted things like imports, again for brevity

If you want to take a look later or follow along in the actual code now you can find it over on my github here

This is based on a fork I made of the original code
Original a couple of years old
Bring up to spec with latest versions (e.g. Serverless)
Make sure it’s still fully deployable if you’d like to try it yourself.
Original link in references at the end

## 22 - Repository layout

I’ll start with a quick overview of the repository layout

aws/
contains function code and serverless manifest for aws
could equally be a gcp folder for example containing Cloud Function code for Google Cloud
flexibility of serverless is being able to deploy to multiple stacks

cmd/
an example command line runner using the github client code

pkg/
go packages that can be shared between functions
allows the functions themselves to stay lightweight and only contain code necessary for a particular platform

resources/
extra things like avatar images that can be used by for example a slack bot

## 23 - The Checker Lambda

The checker service is a fairly vanilla go based lambda.

Entry is as usual via the main function that just involves the Handler() via lambda.Start()

Handler signature depends on configured trigger

Because we’re using destinations all we need to do is return the payload struct and a standard go error type.

A nil error will cause our on_sucess destination (the sqs queue) to be invoked.

Don’t have on_failure configured as no specific handling required, but could post a failed event for example.

## 24 - Structure

Structured as a typical go lambda

## 25 - Env vars

Jumping into the handler:

First thing we do is import the environment variables that we need.

Note: Ideally use a secrets manager for token etc

Importing every invocation - simplest solution for infrequently running lambda

## 26 - Query

Next,

create a client with our access token 
perform the query

These are from my github package which we’ll look at in a moment

Then we can perform rule execution on the results.

In this case we’re simply recording the total number of users in the organisation and how many of them are not configured to use multifactor authentication.
We then put those numbers in the report.

## 27 - Return

And just to finish off, once we have our report, we return it.

Aws takes care of marshaling the report struct to a json

The on_success destination that we configured, in this case an sqs queue means the marshaled report gets automatically published to it - no need to manually connect and publish!

As a last thing, as per normal go, we return a nil error to signify that the lambda has successfully executed.

Depending on how it’s configured, you can use error states to trigger retries or other behaviours.

If we had an on_failure destination configured then a non-nil error would cause that route to be invoked, passing our report payload (populated or nil) along with the error to whichever service was configured to receive it for further processing.

## 28 - The GraphQL Query

Now we’ve seen the checker lambda’s structure, let’s look at the graphQL query

This is split out into a shared module away from the lambda code

so that the code could easily be shared into say, a Google Cloud Function as none of the code contained here is cloud-specific.

## 29 - GraphQL module

For the graphQL calls I’m using Matt Ryer’s machinebox/graphql module.

More complex libraries available with more features
Simple feature set was all I needed

Only configure a single api endpoint for graphql

We handle authentication via an authentication token

Required token scope is in the README

## 30 - The actual query

Quick look at the query

Essentially a fragment of the github graphQL API schema

Some points:

Define variables in the top line (with dollar signs)
These then used in query body
Results are paginated so we grab the next 100 members each time.

Nodes and Edges are how graphql paginates data and they’re a bit of a complicated topic - probably the hardest part of graphql!

## 31 - The Slack Notifier lambda

Once we’ve got a report, we need to do something with it.

This could be anything from raising compliance tickets to firing a confetti cannon, but for the first build I went with a straightforward report to slack

For this I created a webhook integration on slack, from which you get a webhook url to connect to.

## 32 - Notifier structure

Notifier lambda very similar to the checker in structure

Same main() etc

Like we had the CloudWatch event, this time we receive an SQS event 

This contains one or more records to process so we range through them.

Using Slack Block API to build the slack message (on next slide) then post it to the slack API

## 33 - The blocks API

The blocks are represented as a set of json objects

Could template, but here I’m using Go’s powerful json marshaling to build

Several block types exist, for example to include pictures etc.
Here I’m using:

Header - as you’d expect, a heading
Divider - a visual divider for spacing
Section - the main standard content block type
Context - a footer style block

(example on next slide)

## 34 - The output

Finished message looks something like this (depending on your slack theme etc!)

## 35 - Demo

If time allows

## 36 - Thankyou page

n/a

## 37 - References and attributions

n/a
