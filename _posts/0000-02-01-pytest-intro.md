<div class="splash">
<p><tt>pytest</tt> is way too magical</p>
<p class="fragment fade-in">... but in practice this doesn't matter</p>
</div>


Notes:

For those of you in the audience who have considered `pytest`, one common objection is that it is too magical — and we'll get to all the magical stuff it does in a bit. The worry is that it can be hard to reason about `pytest`'s behavior because it's messing around with system code, inspecting the *names* of methods, rewriting byte code.

And I will tell you something as a big proponent of `pytest`: `pytest` is way too magical for my tastes, it's true. But the other thing I'll say is that in practice, this doesn't really matter all that much. If you had shown me `pytest` when it was a young upstart and no one was using it, I would have thought that you were introducing a bunch of implicit behavior, it would lead to terrible technical debt and unmaintainable code. I would have thought that it would never work, but in practice, it's totally working. Pretty much everyone in the open source world uses it, and it's become the industry standard for testing in Python, and none of these dangers have come to pass. It pretty much works!
