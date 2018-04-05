from wit import Wit
import wikipedia as wiki
import sys
import warnings
warnings.filterwarnings("ignore")#I AM SO SORRY ABOUT THIS LINE
# Create the connection to the wit.ai
client = Wit('7WVT67PRB5PVRNOQKXZQBTA5IC7M46HO')

debug = False

#creating seperate arrays, accesible through a common list log
user = 'User'
human = 'human'
friend = 'friend'
log = {
    'human' : [],
    'friend' : [],
}

#memory
article = None# Open article
last_ = -1
contents = None
def fireMemory():
    global article
    global last
    global contents
    if article is None:
        p['fl']('I am not sure I understand...')
        return
    if last is -1:
        #setup for reading extended amounts of an article
        last = 1#an index we can read, skipping the summary
        meta = article.content.replace('==', '=')
        #print(meta)
        meta = meta.replace('==', '=')
        #print(meta)
        contents = meta.split('=')
        #print(contents)
    try:
        if last >= len(contents):
            p['fl']('It seems we have read it all already...')
            return
        else:
            print('\"',end='')
            print(contents[last],end='')
            last = last + 1
            if last >= len(contents):
                print('\"',end='')
                p['fl']('That\'s it.')
                return
            print(contents[last],end='')
            last = last + 1
            print('\"',end='')
    except:
        print('Error:')
        print(contents)
        print(article.content)
    print('')
    # if (last >= len(sects)):
    #    p['fl']('It seems I have read it all')
    #    return

#print out shortcuts
def nl():
    print(" > ", end='')
def fr(var):
    print(" < " + str(var), end='')
def frl(var):
    print(" < " + str(var))
p = {
    'h' : nl , #new line for human input
    'f' : fr , #a print starting with " < ", meaning a robot response
    'fl': frl, # like fr, but with newline at end
}

def debugDumb(human, response):
    print('|-[Debug Spit]---')
    print('|--<Human >--\n|-:\t' + human)
    print('|--<Wit.ai>--')
    for point in response:
        print('|-:\t' + point + ':')
        if (point == 'entities'):
            for entry in response[point]:
                print('|--:\t|   ' + entry + ":")
                for sub_entry in entry[0]:
                    print('|-->\t|-\t ' + str(response[point][entry][0]))
        else:
            print('|-->\t|\t' + response[point])
    print('|-[End]\n')
def getEntity(entity, response):
    if entity in response['entities']:
        return response['entities'][entity][0]['value']
    else:
        return None
def extraction(response):
    extracted = {
        0 : getEntity('intent', response),
        1 : getEntity('wikipedia_search_query', response)
    }
    return extracted

def src(ws, plus):
    # This method makes a search, it will not print out any information about
    # each article, but will attempt to find them at the very least.
    w = wiki.search(ws)
    if len(w) is not 0:
        p['fl']('I found the following articles')
        for e in w:
            p['fl']('\t* ' + str(e))
    else:
        p['fl']('I am sorry, but I found nothing.')
def exp(ws, plus):
    # This method makes a singular search, being very specific
    # It will start reading, prompting an inquiry if the user
    # would like for the WikiFriend to continue

    wcheck = wiki.search(ws)
    global article
    global last
    try:
        w = wiki.page(title=ws)
        article = w
        last = -1
        p['fl']('I found this article,')
        p['fl']('I\'ll just read you the summary:')
        print("\"" + w.summary + "\"\n\t\t\t- Wikipedia")
        p['fl']('Would you like me to continue?')
    except wiki.exceptions.DisambiguationError as list:#catching multiple answers
        try:
            w = wiki.page(title=ws, redirect=False)#made to simply redirect
            article = w
            last = -1
            p['fl']('I found this article,')
            p['fl']('I\'m not sure it\'s what you wanted, but I tried my best...')
            print("\"" + w.summary + "\"\n\t\t\t- Wikipedia")
            p['fl']('Related subjects are...')
            for thing in list.options:
                p['fl']('\t-' + thing)
            p['fl']('Would you like me to read the remainder of the article?')
        except:#Catching anything else... almost anything else
            p['fl']('Odd... , I can\'t seem to find anything.')
            if len(wcheck) is not 0:
                p['fl']('Did you mean any of the following?')
                for src in wcheck:
                    p['fl']('\t' + str(src))
            else:
                p['fl']('Nothing at all...')
def usr(ws, plus):
    global user
    # this will "remember" the username, checking for the earliest one
    for entity in plus:
        if entity == 'contact':
            print(plus[entity])
            user = plus[entity]
            p['fl']('Nice to meet you ' + user + '. How can I help?')
            return
    if ws is not None:# sometimes this
        user = ws
        p['fl']('Nice to meet you ' + user + '. How can I help?')
        return


def bye(ws, plus):
    # this will promt an exit
    p['fl']('Bye ' + user + ', I will be waiting patiently for your return...')
    sys.exit(0)

def dny(ws, plus):
    # This method is a denial, reffering backwards to the last prompts
    p['fl']('Very well, consider it forgotten')
    global article
    article = none

def cnf(ws, plus):
    # This method is a confirmation, reffering backwards to the last prompts
    fireMemory()
def thnx(ws, plus):
    p['fl']('You are most welcome.')
def noIntent(ws, plus):
    #Handles it if the intent is not that easy to discern
    if 'greetings' in plus:
        p['fl']('My name is WikiFriend, do you have a name?')
    else:
        p['fl']('I didn\'t quite get that.')

## Shortcuts, in stead of a switch case, since those don't exist in Python
handle_intent = {
    'search'    : src,
    'explain'   : exp,
    'user'      : usr,
    'goodbye'   : bye,
    'deny'      : dny,
    'confirm'   : cnf,
    'thanks'    : thnx,
    'None'      : noIntent
}

# Runtime code, could just as easily have been fitted into a method,
# but in this case it is slightly redundant.

p['fl']('Hello, how can I help you today?')
while True:#, a nice loop to run around in
    p['h']()
    query = input()#get user input
    robot_response = client.message(query)#get robot response
    # log what we have seen so far
    log[human].append(query)
    log[friend].append(robot_response)
    #
    extract = extraction(robot_response)#Get an extracted message
    if debug: debugDumb(query, robot_response)#Debug information
    if extract[0] is None:
        handle_intent['None'](extract[1], robot_response['entities'])
    else:
        handle_intent[extract[0]](extract[1], robot_response['entities'])
