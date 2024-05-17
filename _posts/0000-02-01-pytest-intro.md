<div class="splash">
<p>✨ <tt>pytest</tt> is way too  magical ✨</p>
<p class="fragment fade-in">... but in practice this doesn't matter</p>
</div>


Notes:

A common objection to `pytest` is that it is way too magical — it selects tests based on their name, it rewrites byte code, it does a bunch of path manipulation and all kinds of magical stuff. The worry people have is that because of the magic, it can be hard to reason abut `pytest`'s behavior.

And I will tell you something as a big proponent of `pytest`: `pytest` is way too magical, it's true. But the other thing I'll say is that in practice, **ADVANCE SLIDE** this doesn't really matter all that much.

If you had shown me `pytest` when it was a young upstart and no one was using it, I would have thought that you were introducing a bunch of implicit behavior, it would lead to terrible technical debt and unmaintainable code, but `pytest` is not a young upstart — it is in fact the standard way to do testing in Python these days, and for good reason, and for the most part I've never seen this magical behavior cause problems. Things mostly just work!
