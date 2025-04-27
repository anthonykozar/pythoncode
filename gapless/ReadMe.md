# Gapless

A domain-specific programming language and Python package for computing with finite groups and group rings.

## Overview

Gapless will be a very simple programming language and CAS (computer algebra system) for computing with any finite group and any group ring/algebra constructed as a free module over the ring of integers (ℤ[G]), the ring of rationals (ℚ[G]), or the ring of real numbers (ℝ[G]) where G is any finite group.  While much more capable CAS's exist for these tasks (notably GAP), Gapless has different goals than existing systems of which I am aware.  Primarily, Gapless is intended to be a much simpler system to use for non-experts such as first-time group theory students and amateur mathematicians.

Specific goals and features will include:

- a focus on computation with the _elements_ of groups and group rings and exploring simple structural properties such as subgroups, cosets, and conjugacy classes. (i.e. There will not be built-in algorithms for topics like derived series, characters, cohomolgy, etc.)

- a syntax as close to common mathematical notations as possible including 

	- multiple, easy-to-type notation options for finite group elements (e.g. numbers, letters, permutations, congruence classes)
	- no commas for permutations and no spaces for small permutations
	- juxtaposition for multiplication & group operations
	- subscripts and superscript powers (using Unicode characters)
	- identifiers for frequently-used groups match their commonly-used notations: ℤ₅, S₃, A₅, D₁₀, etc.
	- generator notation for groups and subgroups (e.g. <(12),(123)>)

- special input methods to ease typing this notation

- an interactive interpreter ("read-eval-print loop") as well as the ability to run non-interactive programs in an interpreter

- user-selectable symbols for group operators chosen from a broad selection of Unicode symbols (e.g. ∘, ⊕, and ⊗)

- group ring elements can be represented as linear combinations of group elements with coefficients (e.g. 5(1) + 2(12) - 3(123), an element of ℤ[S₃]) or as vectors of just the coefficients with an implied canonical order for the group elements (e.g. (5,2,0,0,-3,0) with the order (1), (12), (13), (23), (123), (132) for S₃).

- the ability to designate a "current active group or group ring" that is used for interpreting any notations that would be otherwise ambiguous

- maybe someday a nice cross-platform GUI written in Java (with Gapless running under Jython)

## Colophon

Gapless was specifically conceived on April, 25, 2025 although I had been wishing for an easy-to-use group theory tool for many years.  The name, meaning "without gaps or breaks", is an obvious reference to GAP and implies a desire to do computational group theory without the complexity of GAP.  The name is also somewhat descriptive of the language since group operations can be written with juxtaposition (i.e. "without gaps").

Anthony Kozar

April 27, 2025

http://anthonykozar.net/
