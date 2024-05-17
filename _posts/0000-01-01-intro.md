<div class="centered-container" style="height: 100dvh">
<p class="main-title"><tt>pytest for unittesters</tt></p>

<div class="main-title-info">
<div class="author">
    Paul Ganssle
</div>

<div class="logo">
    <img src="images/pganssle-logos.svg" height="40px" alt="@pganssle">
</div>

<div class="link">
    <span style="font-size: 1em;"><em>This talk on Github:
        <a href="https://github.com/pganssle-talks/2024-pycon-us-pytest">pganssle-talks/2024-pycon-us-pytest</a></em>
    </span>
</div>

<div class="license">
    <a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/">
        <img src="external-images/logos/cc-zero.svg" height="45px">
    </a>
</div>
</div>
</div>

Notes:

Hi everyone, my name is Paul Ganssle, I'm a software engineer at Google and a maintainer of a few open source packages, notably I am a CPython core dev, mostly working on `datetime` and `zoneinfo`.

Today I'm going to be talking about `pytest`, but specifically aimed at audiences who have historically used `unittest` or one of its derivatives. At Google, we tend to use our own derivative of `unittest` called `absltest`, but as a big fan of `pytest`, I wanted to put together a coherent case for why `pytest` is likely a better choice in today's world, and why and how you might want to migrate your `unittest`-based workflow to `pytest`. This talk barely scratches the surface, but I hope that it might highlight some of the advantages of `pytest` for those of you considering a migration, or for those deciding between `unittest` and `pytest` in the first place.
