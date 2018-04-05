== Wit.ai

Why did I choose Wit.ai?
  I looked at multiple, this one was the easiest
  to get a grip on quickly, so I tinkered with it
  until I go an adept enough understanding to
  start programming my solution.

== Implementation:

  1. Atomic perception

    The software uses something I would define as a "soft cheats".

    It only remembers a page (the last one it opened), and the
    users name, if given. Each user input is ATOMIC, meaning that
    for the WikiFriend, full sentences are always required.

  2. Prompted speech and atomic perception

    The wikifriend only prompts the user to two forms of contextual
    input (input in reference to earlier):
       i. A Name.
          If the user greets the wikifriend, the friend will ask if
          you have a name.*
      ii. Confirmation.
          When told to explain something, it will read the wikipedia
          summary (if it can find it), and afterwards ask if it should
          continue to print the information.*

      |* The prompts can be ignored,
      |  due to the atomic perception.

    Reading both confirmation and names is (jf. Implementation 1.) done
    atomicly. Meaning that the prompts can be ignored without side effect,
    and can be triggered without the wikifriend referencing it first.
      (For example you can skip greeting the wikifriend, tell it your name,
      and it will still remember it just fine.)

  3. Overlapping classification

    The WikiFriend tackles terms along the line of "yes", "continue", "go on",
    and "indeed" all as confirmations, as the only reason to give a confirmation
    is to read the next page.

    Of course for more advanced bots, this would be a long term issue for more
    complex refrencing. But for as simple a project as the WikiFriend, this will
    suffice.

  4. Interface

    Currently, the only interface is the terminal (python use).

    I considered giving the bot some success (internal) rating,
    and use this to let the bot emote through the confirmation
    (happy upon a higher score, unhappy with any search failure,
    etc.). I might still do, but not for the time being.
