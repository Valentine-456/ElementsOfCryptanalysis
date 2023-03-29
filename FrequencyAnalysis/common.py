from random import shuffle
import re
import matplotlib.pyplot as plt

def lclear(text):
    return re.sub(r'[^a-z]', '', text.lower())

def generateKeyPair(alphabet: list[str]):
    encodingPermutation = list(range(0, len(alphabet)))
    shuffle(encodingPermutation)

    decodingPermutation = [0 for _ in alphabet]
    for i, value in enumerate(encodingPermutation):
        decodingPermutation[value] = i

    return encodingPermutation, decodingPermutation

def encryptMessage(message: str, publicKey: list[int], alphabet: list[str]) -> str:
    message_lowercase = message.lower()
    ciphertext = ""

    for i in message_lowercase:
        if(i == " "):
            ciphertext = ciphertext + " "
        elif (i not in alphabet):
            continue
        else:
            nextChar = alphabet[publicKey[alphabet.index(i)]]
            ciphertext = ciphertext + nextChar

    return ciphertext

def decryptMessage(ciphertext: str, privateKey: list[int], alphabet: list[str]) -> str:
    return encryptMessage(ciphertext, privateKey, alphabet)



def getFrequencyTable(text: str, alphabet: list[str]) -> dict[str, float]:
    frequencyTable = {}
    for letter in alphabet:
        frequencyTable[letter] = 0
    
    preprocessedText = re.sub(r'[^a-z]', '', text.lower())
    totalLength = len(preprocessedText)
    for i in preprocessedText:
        frequencyTable[i] = frequencyTable[i] + 1
    for key, value in frequencyTable.items():
        frequencyTable[key] = (value/totalLength)
     
    return frequencyTable

def getShortMessage():
    return secretMessage[:150]

def getMediumMessage():
    return secretMessage[:2500]

def getLongMessage():
    return secretMessage

secretMessage = '''
Dear Reader, 

As I sit down to write this letter to you, I feel a mix of emotions - excitement, apprehension, and a hint of nervousness. For you see, this letter carries with it a secret, something that I have never shared with anyone else before. It is a story that I have kept buried deep within me, for fear of what others might think or say. 
But today, I am taking a leap of faith and sharing this story with you, trusting that you will keep my secret safe and sound. It is a story that goes back many years, to a time when I was a young, naive girl with dreams and aspirations, and a thirst for adventure.
Growing up, I was always drawn to the unknown, to the mysteries of the world that lay beyond my reach. I would spend hours lost in books, imagining far-off lands and fantastical creatures, yearning to escape the monotony of my everyday life.
But as I grew older, I realized that my dreams were just that - dreams. The world was not the magical place I had imagined it to be, and I was stuck in a mundane existence that offered me little in the way of excitement or adventure.
It was then that I met him - a man unlike any other I had ever known. He was charismatic, charming, and possessed a sense of mystery that drew me in like a moth to a flame. We met quite by chance, at a party where I was feeling out of place and awkward, and he seemed to take pity on me, striking up a conversation that soon had us both laughing and talking like old friends.
Over the next few weeks, we saw each other often, going out for dinners, walks in the park, and even a few weekend getaways. He introduced me to a world that was completely new to me, a world of adventure and excitement that I had only ever dreamed of.
But as time went on, I began to realize that there was more to him than met the eye. He would disappear for days on end, leaving me wondering where he was and what he was doing. And then he would show up again, as if nothing had happened, with a smile on his face and a new story to tell.
I knew that something was not quite right, but I was so drawn to him that I couldn't bring myself to walk away. And then, one day, he asked me to do something that I knew was wrong, something that would put me in danger if I were caught.
I won't go into the details of what he asked me to do, for fear of incriminating myself or others. But suffice it to say that it was a turning point in our relationship. I realized then that he was not the man I thought he was, that his sense of adventure and excitement was not worth the risk of getting caught and facing the consequences.
I walked away from him that day, never looking back. But the memory of him has stayed with me all these years, a reminder of a time in my life when I was young and foolish, when I thought that anything was possible.
And so, dear reader, I entrust you with my secret, with the knowledge of a time in my life that I have never shared with anyone else. I ask only that you keep it safe and sound, that you do not judge me for my actions, and that you remember that we are all human, flawed and imperfect, but still deserving of love and forgiveness.

Yours sincerely,
A Secret Keeper

Dear Secret Keeper,

I received your letter with a mix of surprise and curiosity. It is rare to receive such a personal and intimate message from someone, and I appreciate the trust that you have placed in me by sharing your story.
First and foremost, I want to assure you that I will keep your secret safe and confidential. I understand that sharing something so personal and private can be daunting, and I want you to know that you can trust me to respect your wishes and keep your story between us.
I can imagine how difficult it must have been for you to live through such a challenging and complex situation. It is never easy to navigate the gray areas of life, to find ourselves confronted with situations that challenge our morals and beliefs.
I commend you for your courage and strength in walking away from the man who asked you to do something that you knew was wrong. It takes a great deal of courage to stand up for what we believe in, to recognize when something is not right and to take action to protect ourselves and those around us.
Your story is a reminder that we all have our secrets, our vulnerabilities, and our flaws. We are all human, and we all make mistakes. What matters most is how we choose to respond to these challenges, how we learn from our experiences, and how we grow as individuals.
I hope that by sharing your story with me, you have found a sense of release and closure. It takes courage to open up to others, to share our vulnerabilities and to trust that we will be understood and supported.
Please know that you are not alone, and that there are many people in this world who are going through similar challenges and experiences. It is through sharing our stories, our secrets, and our vulnerabilities that we can connect with others, build meaningful relationships, and find the strength to keep moving forward.
Thank you for entrusting me with your secret. I feel honored to have received your letter, and I hope that you will find peace and solace in knowing that you are not alone.

Sincerely,
A Caring Friend

Yes; there had been things in his boyhood that he had not understood.
He understood them now. Life suddenly became fiery-coloured to him. It
seemed to him that he had been walking in fire. Why had he not known
it?

With his subtle smile, Lord Henry watched him. He knew the precise
psychological moment when to say nothing. He felt intensely interested.
He was amazed at the sudden impression that his words had produced,
and, remembering a book that he had read when he was sixteen, a book
which had revealed to him much that he had not known before, he
wondered whether Dorian Gray was passing through a similar experience.
He had merely shot an arrow into the air. Had it hit the mark? How
fascinating the lad was!

Hallward painted away with that marvellous bold touch of his, that had
the true refinement and perfect delicacy that in art, at any rate comes
only from strength. He was unconscious of the silence.

“Basil, I am tired of standing,” cried Dorian Gray suddenly. “I must go
out and sit in the garden. The air is stifling here.”

“My dear fellow, I am so sorry. When I am painting, I can’t think of
anything else. But you never sat better. You were perfectly still. And
I have caught the effect I wanted—the half-parted lips and the bright
look in the eyes. I don’t know what Harry has been saying to you, but
he has certainly made you have the most wonderful expression. I suppose
he has been paying you compliments. You mustn’t believe a word that he
says.”

“He has certainly not been paying me compliments. Perhaps that is the
reason that I don’t believe anything he has told me.”

“You know you believe it all,” said Lord Henry, looking at him with his
dreamy languorous eyes. “I will go out to the garden with you. It is
horribly hot in the studio. Basil, let us have something iced to drink,
something with strawberries in it.”

“Certainly, Harry. Just touch the bell, and when Parker comes I will
tell him what you want. I have got to work up this background, so I
will join you later on. Don’t keep Dorian too long. I have never been
in better form for painting than I am to-day. This is going to be my
masterpiece. It is my masterpiece as it stands.”

Lord Henry went out to the garden and found Dorian Gray burying his
face in the great cool lilac-blossoms, feverishly drinking in their
perfume as if it had been wine. He came close to him and put his hand
upon his shoulder. “You are quite right to do that,” he murmured.
“Nothing can cure the soul but the senses, just as nothing can cure the
senses but the soul.”

The lad started and drew back. He was bareheaded, and the leaves had
tossed his rebellious curls and tangled all their gilded threads. There
was a look of fear in his eyes, such as people have when they are
suddenly awakened. His finely chiselled nostrils quivered, and some
hidden nerve shook the scarlet of his lips and left them trembling.

“Yes,” continued Lord Henry, “that is one of the great secrets of
life—to cure the soul by means of the senses, and the senses by means
of the soul. You are a wonderful creation. You know more than you think
you know, just as you know less than you want to know.”

Dorian Gray frowned and turned his head away. He could not help liking
the tall, graceful young man who was standing by him. His romantic,
olive-coloured face and worn expression interested him. There was
something in his low languid voice that was absolutely fascinating. His
cool, white, flowerlike hands, even, had a curious charm. They moved,
as he spoke, like music, and seemed to have a language of their own.
But he felt afraid of him, and ashamed of being afraid. Why had it been
left for a stranger to reveal him to himself? He had known Basil
Hallward for months, but the friendship between them had never altered
him. Suddenly there had come some one across his life who seemed to
have disclosed to him life’s mystery. And, yet, what was there to be
afraid of? He was not a schoolboy or a girl. It was absurd to be
frightened.

“You will excuse this mask,” continued our strange visitor. “The august
person who employs me wishes his agent to be unknown to you, and I may
confess at once that the title by which I have just called myself is
not exactly my own.”

“I was aware of it,” said Holmes dryly.

“The circumstances are of great delicacy, and every precaution has to
be taken to quench what might grow to be an immense scandal and
seriously compromise one of the reigning families of Europe. To speak
plainly, the matter implicates the great House of Ormstein, hereditary
kings of Bohemia.”

“I was also aware of that,” murmured Holmes, settling himself down in
his armchair and closing his eyes.

Our visitor glanced with some apparent surprise at the languid,
lounging figure of the man who had been no doubt depicted to him as the
most incisive reasoner and most energetic agent in Europe. Holmes
slowly reopened his eyes and looked impatiently at his gigantic client.

“If your Majesty would condescend to state your case,” he remarked, “I
should be better able to advise you.”

The man sprang from his chair and paced up and down the room in
uncontrollable agitation. Then, with a gesture of desperation, he tore
the mask from his face and hurled it upon the ground. “You are right,”
he cried; “I am the King. Why should I attempt to conceal it?”

“Why, indeed?” murmured Holmes. “Your Majesty had not spoken before I
was aware that I was addressing Wilhelm Gottsreich Sigismond von
Ormstein, Grand Duke of Cassel-Felstein, and hereditary King of
Bohemia.”

“But you can understand,” said our strange visitor, sitting down once
more and passing his hand over his high white forehead, “you can
understand that I am not accustomed to doing such business in my own
person. Yet the matter was so delicate that I could not confide it to
an agent without putting myself in his power. I have come _incognito_
from Prague for the purpose of consulting you.”

“Then, pray consult,” said Holmes, shutting his eyes once more.

“The facts are briefly these: Some five years ago, during a lengthy
visit to Warsaw, I made the acquaintance of the well-known adventuress,
Irene Adler. The name is no doubt familiar to you.”

“Kindly look her up in my index, Doctor,” murmured Holmes without
opening his eyes. For many years he had adopted a system of docketing
all paragraphs concerning men and things, so that it was difficult to
name a subject or a person on which he could not at once furnish
information. In this case I found her biography sandwiched in between
that of a Hebrew rabbi and that of a staff-commander who had written a
monograph upon the deep-sea fishes.

“Let me see!” said Holmes. “Hum! Born in New Jersey in the year 1858.
Contralto—hum! La Scala, hum! Prima donna Imperial Opera of Warsaw—yes!
Retired from operatic stage—ha! Living in London—quite so! Your
Majesty, as I understand, became entangled with this young person,
wrote her some compromising letters, and is now desirous of getting
those letters back.”

“Precisely so. But how—”

“Was there a secret marriage?”

“None.”

“No legal papers or certificates?”

“None.”

“Then I fail to follow your Majesty. If this young person should
produce her letters for blackmailing or other purposes, how is she to
prove their authenticity?”

“There is the writing.”

“Pooh, pooh! Forgery.”

“My private note-paper.”

“Stolen.”

“My own seal.”

“Imitated.”

“My photograph.”

“Bought.”

“We were both in the photograph.”

“Oh, dear! That is very bad! Your Majesty has indeed committed an
indiscretion.”

“I was mad—insane.”

“You have compromised yourself seriously.”

“I was only Crown Prince then. I was young. I am but thirty now.”

“It must be recovered.”

“We have tried and failed.”

“Your Majesty must pay. It must be bought.”

“She will not sell.”

“Stolen, then.”

“Five attempts have been made. Twice burglars in my pay ransacked her
house. Once we diverted her luggage when she travelled. Twice she has
been waylaid. There has been no result.”

“No sign of it?”

“Absolutely none.”

Holmes laughed. “It is quite a pretty little problem,” said he.

“But a very serious one to me,” returned the King reproachfully.

“Very, indeed. And what does she propose to do with the photograph?”

“To ruin me.”

“But how?”

“I am about to be married.”

“So I have heard.”

“To Clotilde Lothman von Saxe-Meningen, second daughter of the King of
Scandinavia. You may know the strict principles of her family. She is
herself the very soul of delicacy. A shadow of a doubt as to my conduct
would bring the matter to an end.”

“And Irene Adler?”

“Threatens to send them the photograph. And she will do it. I know that
she will do it. You do not know her, but she has a soul of steel. She
has the face of the most beautiful of women, and the mind of the most
resolute of men. Rather than I should marry another woman, there are no
lengths to which she would not go—none.”

“You are sure that she has not sent it yet?”

“I am sure.”

“And why?”

“Because she has said that she would send it on the day when the
betrothal was publicly proclaimed. That will be next Monday.”

“Oh, then we have three days yet,” said Holmes with a yawn. “That is
very fortunate, as I have one or two matters of importance to look into
just at present. Your Majesty will, of course, stay in London for the
present?”

“Certainly. You will find me at the Langham under the name of the Count
Von Kramm.”

“Then I shall drop you a line to let you know how we progress.”

“Pray do so. I shall be all anxiety.”

“Then, as to money?”

“You have _carte blanche_.”

“Absolutely?”

“I tell you that I would give one of the provinces of my kingdom to
have that photograph.”

“And for present expenses?”

The King took a heavy chamois leather bag from under his cloak and laid
it on the table.

“There are three hundred pounds in gold and seven hundred in notes,” he
said.

Holmes scribbled a receipt upon a sheet of his note-book and handed it
to him.

“And Mademoiselle’s address?” he asked.

“Is Briony Lodge, Serpentine Avenue, St. John’s Wood.”

Holmes took a note of it. “One other question,” said he. “Was the
photograph a cabinet?”

“It was.”

“Then, good-night, your Majesty, and I trust that we shall soon have
some good news for you. And good-night, Watson,” he added, as the
wheels of the royal brougham rolled down the street. “If you will be
good enough to call to-morrow afternoon at three o’clock I should like
to chat this little matter over with you.”


II.

At three o’clock precisely I was at Baker Street, but Holmes had not
yet returned. The landlady informed me that he had left the house
shortly after eight o’clock in the morning. I sat down beside the fire,
however, with the intention of awaiting him, however long he might be.
I was already deeply interested in his inquiry, for, though it was
surrounded by none of the grim and strange features which were
associated with the two crimes which I have already recorded, still,
the nature of the case and the exalted station of his client gave it a
character of its own. Indeed, apart from the nature of the
investigation which my friend had on hand, there was something in his
masterly grasp of a situation, and his keen, incisive reasoning, which
made it a pleasure to me to study his system of work, and to follow the
quick, subtle methods by which he disentangled the most inextricable
mysteries. So accustomed was I to his invariable success that the very
possibility of his failing had ceased to enter into my head.

It was close upon four before the door opened, and a drunken-looking
groom, ill-kempt and side-whiskered, with an inflamed face and
disreputable clothes, walked into the room. Accustomed as I was to my
friend’s amazing powers in the use of disguises, I had to look three
times before I was certain that it was indeed he. With a nod he
vanished into the bedroom, whence he emerged in five minutes
tweed-suited and respectable, as of old. Putting his hands into his
pockets, he stretched out his legs in front of the fire and laughed
heartily for some minutes.

“Well, really!” he cried, and then he choked and laughed again until he
was obliged to lie back, limp and helpless, in the chair.

“What is it?”

“It’s quite too funny. I am sure you could never guess how I employed
my morning, or what I ended by doing.”

“I can’t imagine. I suppose that you have been watching the habits, and
perhaps the house, of Miss Irene Adler.”

“Quite so; but the sequel was rather unusual. I will tell you, however.
I left the house a little after eight o’clock this morning in the
character of a groom out of work. There is a wonderful sympathy and
freemasonry among horsey men. Be one of them, and you will know all
that there is to know. I soon found Briony Lodge. It is a _bijou_
villa, with a garden at the back, but built out in front right up to
the road, two stories. Chubb lock to the door. Large sitting-room on
the right side, well furnished, with long windows almost to the floor,
and those preposterous English window fasteners which a child could
open. Behind there was nothing remarkable, save that the passage window
could be reached from the top of the coach-house. I walked round it and
examined it closely from every point of view, but without noting
anything else of interest.

“I then lounged down the street and found, as I expected, that there
was a mews in a lane which runs down by one wall of the garden. I lent
the ostlers a hand in rubbing down their horses, and received in
exchange twopence, a glass of half-and-half, two fills of shag tobacco,
and as much information as I could desire about Miss Adler, to say
nothing of half a dozen other people in the neighbourhood in whom I was
not in the least interested, but whose biographies I was compelled to
listen to.”

“And what of Irene Adler?” I asked.

“Oh, she has turned all the men’s heads down in that part. She is the
daintiest thing under a bonnet on this planet. So say the
Serpentine-mews, to a man. She lives quietly, sings at concerts, drives
out at five every day, and returns at seven sharp for dinner. Seldom
goes out at other times, except when she sings. Has only one male
visitor, but a good deal of him. He is dark, handsome, and dashing,
never calls less than once a day, and often twice. He is a Mr. Godfrey
Norton, of the Inner Temple. See the advantages of a cabman as a
confidant. They had driven him home a dozen times from Serpentine-mews,
and knew all about him. When I had listened to all they had to tell, I
began to walk up and down near Briony Lodge once more, and to think
over my plan of campaign.

“Well, then, with the first money I touch, I mean you to have a small
house, with a garden in which to plant clematis, nasturtiums, and
honeysuckle. But what ails you, father? Are you not well?”

“’Tis nothing, nothing; it will soon pass away”—and as he said so the
old man’s strength failed him, and he fell backwards.

“Come, come,” said the young man, “a glass of wine, father, will revive
you. Where do you keep your wine?”

“No, no; thanks. You need not look for it; I do not want it,” said the
old man.

“Yes, yes, father, tell me where it is,” and he opened two or three
cupboards.

“It is no use,” said the old man, “there is no wine.”

“What, no wine?” said Dantès, turning pale, and looking alternately at
the hollow cheeks of the old man and the empty cupboards. “What, no
wine? Have you wanted money, father?”

“I want nothing now that I have you,” said the old man.

“Yet,” stammered Dantès, wiping the perspiration from his brow,—“yet I
gave you two hundred francs when I left, three months ago.”

“Yes, yes, Edmond, that is true, but you forgot at that time a little
debt to our neighbor, Caderousse. He reminded me of it, telling me if I
did not pay for you, he would be paid by M. Morrel; and so, you see,
lest he might do you an injury——”

“Well?”

“Why, I paid him.”

“But,” cried Dantès, “it was a hundred and forty francs I owed
Caderousse.”

“Yes,” stammered the old man.

“And you paid him out of the two hundred francs I left you?”

The old man nodded.

“So that you have lived for three months on sixty francs,” muttered
Edmond.

“You know how little I require,” said the old man.

“Heaven pardon me,” cried Edmond, falling on his knees before his
father.

“What are you doing?”

“You have wounded me to the heart.”

“Never mind it, for I see you once more,” said the old man; “and now
it’s all over—everything is all right again.”

0035m



“Yes, here I am,” said the young man, “with a promising future and a
little money. Here, father, here!” he said, “take this—take it, and
send for something immediately.” And he emptied his pockets on the
table, the contents consisting of a dozen gold pieces, five or six
five-franc pieces, and some smaller coin. The countenance of old Dantès
brightened.

“Whom does this belong to?” he inquired.

“To me, to you, to us! Take it; buy some provisions; be happy, and
tomorrow we shall have more.”

“Gently, gently,” said the old man, with a smile; “and by your leave I
will use your purse moderately, for they would say, if they saw me buy
too many things at a time, that I had been obliged to await your
return, in order to be able to purchase them.”

“Do as you please; but, first of all, pray have a servant, father. I
will not have you left alone so long. I have some smuggled coffee and
most capital tobacco, in a small chest in the hold, which you shall
have tomorrow. But, hush, here comes somebody.”

“’Tis Caderousse, who has heard of your arrival, and no doubt comes to
congratulate you on your fortunate return.”

“Ah, lips that say one thing, while the heart thinks another,” murmured
Edmond. “But, never mind, he is a neighbor who has done us a service on
a time, so he’s welcome.”

As Edmond paused, the black and bearded head of Caderousse appeared at
the door. He was a man of twenty-five or six, and held a piece of
cloth, which, being a tailor, he was about to make into a coat-lining.

“What, is it you, Edmond, back again?” said he, with a broad
Marseillaise accent, and a grin that displayed his ivory-white teeth.

“Yes, as you see, neighbor Caderousse; and ready to be agreeable to you
in any and every way,” replied Dantès, but ill-concealing his coldness
under this cloak of civility.

“Thanks—thanks; but, fortunately, I do not want for anything; and it
chances that at times there are others who have need of me.” Dantès
made a gesture. “I do not allude to you, my boy. No!—no! I lent you
money, and you returned it; that’s like good neighbors, and we are
quits.”

“We are never quits with those who oblige us,” was Dantès’ reply; “for
when we do not owe them money, we owe them gratitude.”

“What’s the use of mentioning that? What is done is done. Let us talk
of your happy return, my boy. I had gone on the quay to match a piece
of mulberry cloth, when I met friend Danglars. ‘You at
Marseilles?’—‘Yes,’ says he.

“‘I thought you were at Smyrna.’—‘I was; but am now back again.’

“‘And where is the dear boy, our little Edmond?’

“‘Why, with his father, no doubt,’ replied Danglars. And so I came,”
added Caderousse, “as fast as I could to have the pleasure of shaking
hands with a friend.”

0037m



“Worthy Caderousse!” said the old man, “he is so much attached to us.”

“Yes, to be sure I am. I love and esteem you, because honest folks are
so rare. But it seems you have come back rich, my boy,” continued the
tailor, looking askance at the handful of gold and silver which Dantès
had thrown on the table.

The young man remarked the greedy glance which shone in the dark eyes
of his neighbor. “Eh,” he said, negligently, “this money is not mine. I
was expressing to my father my fears that he had wanted many things in
my absence, and to convince me he emptied his purse on the table. Come,
father” added Dantès, “put this money back in your box—unless neighbor
Caderousse wants anything, and in that case it is at his service.”

“No, my boy, no,” said Caderousse. “I am not in any want, thank God, my
living is suited to my means. Keep your money—keep it, I say;—one never
has too much;—but, at the same time, my boy, I am as much obliged by
your offer as if I took advantage of it.”

“It was offered with good will,” said Dantès.

“No doubt, my boy; no doubt. Well, you stand well with M. Morrel I
hear,—you insinuating dog, you!”

“M. Morrel has always been exceedingly kind to me,” replied Dantès.

“Then you were wrong to refuse to dine with him.”

“What, did you refuse to dine with him?” said old Dantès; “and did he
invite you to dine?”

“Yes, my dear father,” replied Edmond, smiling at his father’s
astonishment at the excessive honor paid to his son.

“And why did you refuse, my son?” inquired the old man.

“That I might the sooner see you again, my dear father,” replied the
young man. “I was most anxious to see you.”

“But it must have vexed M. Morrel, good, worthy man,” said Caderousse.
“And when you are looking forward to be captain, it was wrong to annoy
the owner.”

“But I explained to him the cause of my refusal,” replied Dantès, “and
I hope he fully understood it.”

“Yes, but to be captain one must do a little flattery to one’s
patrons.”

“I hope to be captain without that,” said Dantès.

“So much the better—so much the better! Nothing will give greater
pleasure to all your old friends; and I know one down there behind the
Saint Nicolas citadel who will not be sorry to hear it.”
'''