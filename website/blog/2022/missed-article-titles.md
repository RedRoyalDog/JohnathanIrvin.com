---
title: Forgotten Article Titles
date: 2022-08-12
description: Article titles disappeared from the website titling after the rewrite. A simple mistake correlated to feature parity when rewriting software in a corporate setting. The fix prevents future regressions.
---

After spending weeks on a rewrite of the website, I was excited to take a small break from working on my blog.

Google analytics informed me that all of my pages bore the same title. Such a simple mistake caused me a headache. The landing page was indistinguishable from the blog posts. 

I needed to confirm if my content was engaging and read by the user.

## Table Of Contents

[TOC]

## Simple Solution

Blocks, such as the title, can be overridden in the layout. The `block` tag accepts the `title` as a parameter.

The default looks like this:

```pugjs
block title
    title Engineer, Researcher, Entrepreneur - Johnathan Irvin
```

The layout contains the default title. I overrode the block in the `article.pug` file.

```
pugjs
block title
    title {{ title }} - Johnathan Irvin
```

Notice the `title` is wrapped in `{{` and `}}`. We pass this variable via [flask](https://flask.palletsprojects.com/) to the [jinja](https://jinja.palletsprojects.com) template before rendering.

See the [merge request](https://github.com/JohnnyIrvin/Website/pull/50/files) for the full solution.

## Never Again

As your codebase grows, the risk of introducing regressions also increases. Regressions are errors that occur after a change is made to the code, and they can be difficult to track down and fix. Automated testing can help prevent regressions by catching errors before they are introduced into the code.

There are different types of automated tests, but unit tests are the most important for preventing regressions. A unit test is a small test that covers a single piece of code, and it is typically written by the developer who wrote the code. Unit tests exercise the code to make sure it behaves as expected.

If a test fails, the code has regressed. By running the tests automatically, regressions are caught early, before they make it into the codebase.

In addition to unit tests, you can also use integration tests and regression tests. Integration tests test how different parts of the code work together, and regression tests test the code for changes that could introduce regressions.

Snapshot tests are a great way to ensure that your UI does not break unexpectedly. Snapshot tests are the quickest to write and easily catch regression bugs.

I am lazy and chose to write snapshot tests. See this [commit](https://github.com/JohnnyIrvin/Website/commit/42a5402bdac82a950d9d9ef3cc10a6743431ab2e) to see these tests.

## Automation Golemns

Automated testing is a process where automation tools execute software tests without manual intervention. The process improves the quality of the software and ensures that it meets the required standards.

Benefits of automated testing include:

1. Improved software accuracy by eliminating human error.

2. Increased efficiency by reducing the time required to execute tests.

3. Increased coverage by increasing the number of tests in a period.

4. Reduced costs by removing human effort.

5. Increased quality by meeting required standards.

I used GitHub Actions to automate the testing process. See the [merge request](https://github.com/JohnnyIrvin/Website/pull/52/files) for the full solution.
