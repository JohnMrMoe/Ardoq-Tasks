Criteria 1: The chatbout should include at least 2 commands
  Well, it sort of has several:
    1. Explain
    2. Search
    3. User
    4. Responses
      i. confirm
      ii. deny
    4. Miscellaneous others...
      i. greeting
      ii. goodbye



      ////////////////////////////////////////////////////////////////////////////////
Criteria 2: One of the commands should give a follow-up question.
  The command 'explain'* extracts your search words, and finds
  the wikipedia page for it (or, the redirected one if that fails (or
  a polite "error" if nothing is found)). It will print the summary of the page,
  before asking the user if they would like to read further.

  The user can then respond in method that would trigger the 'confirm'** command.
  This will *attempt* to print out the two next sections, separated by '=', '==',
  or '===' signs.

  If the user responds with anything that would fit under deny, the bot will
  clear the page it has open currently.
    This is superfluous, as a new search will overwrite the old one.
    It is made even more superfluous by the fact that the prompt is always open
    to all commands, meaning that one doesn't actually have to respond to the inquiry.

  *Can be prompted with sentences like: "tell me about X", "what do you know about X", etc.
  **Can be prompted with triggers like "yes", "continue", "go on"


////////////////////////////////////////////////////////////////////////////////
Criteria 3: One of the commands should give an answer from a public API (i.e. Yr,
    Coindesk, The Internet Chuck Norris Database, ...)

  I elected the Wikipedia API, both search and explain use both this api, and the wit.ai api.



////////////////////////////////////////////////////////////////////////////////
Criteria 4: Sample conversation
  NB: As in the program: "<" is the predicate of the bots reply, and ">" of the human input

< Hello
> Hello
< My name is WikiFriend, do you have a name?
