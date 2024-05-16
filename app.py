# import the libraries

import math
import numpy as np
import pickle
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
# from streamlit_extras.stylable_container import stylable_container
import os
import random
import utils as utl
import warnings
warnings.filterwarnings("ignore")

# from librosa import librosa
# SET PAGE WIDE

def get_songs(genre):
    # songs = {
    songs = {
    'blues': ['The Thrill is Gone - B.B. King', 'Mannish Boy - Muddy Waters', 'Sweet Little Angel - Lucille Bogan', 'I Cant Quit You Baby - Willie Dixon', 'Love In Vain - Robert Johnson', 'Boogie Chillen - John Lee Hooker', 'Statesboro Blues - Blind Willie McTell', 'Hellhound On My Trail - Robert Johnson', 'Smokestack Lightnin - Howlin Wolf', 'Pride and Joy - Stevie Ray Vaughan', 'Cross Road Blues - Robert Johnson', 'Hoochie Coochie Man - Muddy Waters', 'Me and the Devil Blues - Robert Johnson', 'Stone Crazy - Buddy Guy', 'I\'m Tore Down - Freddie King', 'Born Under a Bad Sign - Albert King', 'Mustang Sally - Wilson Pickett', 'Black Betty - Lead Belly', 'Need Your Love So Bad - Little Willie John', 'I\'d Rather Go Blind - Etta James', 'Texas Flood - Stevie Ray Vaughan', 'I\'m Ready - Muddy Waters', 'The Sky Is Crying - Elmore James', 'Reconsider Baby - Lowell Fulson', 'It Serves Me Right to Suffer - John Lee Hooker', 'Got My Mojo Working - Muddy Waters', 'Key to the Highway - Big Bill Broonzy', 'Juke - Little Walter', 'They Call It Stormy Monday - T-Bone Walker', 'Boom Boom - John Lee Hooker'],
    'classical': [ "Symphony No. 5 - Ludwig van Beethoven","The Four Seasons - Antonio Vivaldi","Eine kleine Nachtmusik - Wolfgang Amadeus Mozart","Prelude to the Afternoon of a Faun - Claude Debussy","The Nutcracker - Pyotr Ilyich Tchaikovsky","Swan Lake - Pyotr Ilyich Tchaikovsky","Four Pieces for String Quartet - Anton Webern","Sonata for Two Pianos - Igor Stravinsky","Concerto for Orchestra - Béla Bartók","Symphony No. 9 - Gustav Mahler","Symphony No. 40 - Wolfgang Amadeus Mozart","Symphony No. 3 - Ludwig van Beethoven","Symphony No. 9 - Antonín Dvořák","Brandenburg Concertos - Johann Sebastian Bach","Rhapsody in Blue - George Gershwin","Boléro - Maurice Ravel","Carmina Burana - Carl Orff","Piano Concerto No. 1 - Pyotr Ilyich Tchaikovsky","The Planets - Gustav Holst","Cello Concerto - Edward Elgar","The Firebird - Igor Stravinsky","Symphony No. 7 - Ludwig van Beethoven","The Rite of Spring - Igor Stravinsky","Carmen - Georges Bizet","The Magic Flute - Wolfgang Amadeus Mozart","Don Giovanni - Wolfgang Amadeus Mozart","The Marriage of Figaro - Wolfgang Amadeus Mozart","La Traviata - Giuseppe Verdi","Turandot - Giacomo Puccini","The Barber of Seville - Gioachino Rossini","The Valkyrie: Ride of the Valkyries - Richard Wagner","Symphony No. 25 - Wolfgang Amadeus Mozart","The Barber of Seville: Overture - Gioachino Rossini","Symphony No. 9 (From the New World) - Antonín Dvořák","Piano Sonata No. 11 (Rondo Alla Turca) - Wolfgang Amadeus Mozart","Symphony No. 41 (Jupiter Symphony) - Wolfgang Amadeus Mozart","Piano Sonata No. 14 (Moonlight Sonata) - Ludwig van Beethoven","Symphony No. 5 - Ludwig van Beethoven","Symphony No. 7 - Ludwig van Beethoven","Symphony No. 9 (Choral Symphony) - Ludwig van Beethoven","Für Elise - Ludwig van Beethoven","Violin Concerto in E minor - Felix Mendelssohn","The Four Seasons: Spring - Antonio Vivaldi","The Four Seasons: Summer - Antonio Vivaldi","The Four Seasons: Autumn - Antonio Vivaldi","The Four Seasons: Winter - Antonio Vivaldi","Water Music - George Frideric Handel","Music for the Royal Fireworks - George Frideric Handel","Messiah: Hallelujah Chorus - George Frideric Handel","Brandenburg Concerto No. 3 - Johann Sebastian Bach","Brandenburg Concerto No. 4 - Johann Sebastian Bach","Brandenburg Concerto No. 5 - Johann Sebastian Bach","Canon in D - Johann Pachelbel","Air on the G String - Johann Sebastian Bach","Moonlight Sonata - Ludwig van Beethoven","Clair de Lune - Claude Debussy","Prelude in C Major - Johann Sebastian Bach","Nocturne in E-flat Major - Frédéric Chopin","The Blue Danube - Johann Strauss II", "Ode to Joy - Ludwig van Beethoven","Toccata and Fugue in D minor - Johann Sebastian Bach","Hungarian Dance No. 5 - Johannes Brahms","Symphony No. 94 (Surprise Symphony) - Joseph Haydn","William Tell Overture - Gioachino Rossini","The Valkyrie: Ride of the Valkyries - Richard Wagner","Symphony No. 25 - Wolfgang Amadeus Mozart","The Barber of Seville: Overture - Gioachino Rossini","Symphony No. 9 (From the New World) - Antonín Dvořák","Piano Sonata No. 11 (Rondo Alla Turca) - Wolfgang Amadeus Mozart", "Symphony No. 41 (Jupiter Symphony) - Wolfgang Amadeus Mozart","Piano Concerto No. 21 - Wolfgang Amadeus Mozart", "The Magic Flute: Overture - Wolfgang Amadeus Mozart","Eine Kleine Nachtmusik: Allegro - Wolfgang Amadeus Mozart","Piano Sonata No. 14 (Moonlight Sonata) - Ludwig van Beethoven", "Symphony No. 5 - Ludwig van Beethoven","Symphony No. 7 - Ludwig van Beethoven","Symphony No. 9 (Choral Symphony) - Ludwig van Beethoven","Fur Elise - Ludwig van Beethoven","Violin Concerto in E minor - Felix Mendelssohn", "The Four Seasons: Spring - Antonio Vivaldi","The Four Seasons: Summer - Antonio Vivaldi", "The Four Seasons: Autumn - Antonio Vivaldi","The Four Seasons: Winter - Antonio Vivaldi","Water Music - George Frideric Handel","Music for the Royal Fireworks - George Frideric Handel","Messiah: Hallelujah Chorus - George Frideric Handel","Brandenburg Concerto No. 3 - Johann Sebastian Bach","Brandenburg Concerto No. 4 - Johann Sebastian Bach","Brandenburg Concerto No. 5 - Johann Sebastian Bach","Orchestral Suite No. 3: Air - Johann Sebastian Bach","The Well-Tempered Clavier: Prelude in C Major - Johann Sebastian Bach","Toccata and Fugue in D minor - Johann Sebastian Bach","Cello Suite No. 1: Prelude - Johann Sebastian Bach","The Art of Fugue - Johann Sebastian Bach","Goldberg Variations - Johann Sebastian Bach","Mass in B minor - Johann Sebastian Bach","St. Matthew Passion - Johann Sebastian Bach","Christmas Oratorio - Johann Sebastian Bach","Magnificat in D major - Johann Sebastian Bach","Italian Concerto - Johann Sebastian Bach","French Suite No. 5 - Johann Sebastian Bach","English Suite No. 3 - Johann Sebastian Bach",'Symphony No. 5 - Beethoven', 'The Four Seasons - Vivaldi', 'Eine kleine Nachtmusik - Mozart', 'Prelude to the Afternoon of a Faun - Debussy', 'The Nutcracker - Tchaikovsky', 'Swan Lake - Tchaikovsky', 'Four Pieces for String Quartet - Webern', 'Sonata for Two Pianos - Stravinsky', 'Concerto for Orchestra - Bartok', 'Symphony No. 9 - Mahler', 'Symphony No. 40 - Mozart', 'Symphony No. 3 - Beethoven', 'Symphony No. 9 - Dvorak', 'Brandenburg Concertos - Bach', 'Rhapsody in Blue - Gershwin', 'Bolero - Ravel', 'Carmina Burana - Orff', 'Piano Concerto No. 1 - Tchaikovsky', 'The Planets - Holst', 'Cello Concerto - Elgar', 'The Firebird - Stravinsky', 'Symphony No. 7 - Beethoven', 'The Rite of Spring - Stravinsky', 'Carmen - Bizet', 'The Magic Flute - Mozart', 'Don Giovanni - Mozart', 'The Marriage of Figaro - Mozart', 'La Traviata - Verdi', 'Turandot - Puccini', 'The Barber of Seville - Rossini'],
    'country': [ "Amarillo by Morning - George Strait","The Dance - Garth Brooks","I Will Always Love You - Dolly Parton","He Stopped Loving Her Today - George Jones","Crazy - Patsy Cline","Your Cheatin' Heart - Hank Williams","Mama Tried - Merle Haggard","I'm So Lonesome I Could Cry - Hank Williams","Blue Eyes Crying in the Rain - Willie Nelson","Coal Miner's Daughter - Loretta Lynn","The Gambler - Kenny Rogers","Ring of Fire - Johnny Cash","Hello Darlin' - Conway Twitty","Stand by Your Man - Tammy Wynette","Go Rest High on That Mountain - Vince Gill","Wide Open Spaces - Dixie Chicks","I Hope You Dance - Lee Ann Womack","Where Were You (When the World Stopped Turning) - Alan Jackson","Live Like You Were Dying - Tim McGraw","Jolene - Dolly Parton","Take Me Home, Country Roads - John Denver","Friends in Low Places - Garth Brooks","I Walk the Line - Johnny Cash","Folsom Prison Blues - Johnny Cash","Always on My Mind - Willie Nelson","On the Road Again - Willie Nelson","Dirt Road Anthem - Jason Aldean","Need You Now - Lady A","Before He Cheats - Carrie Underwood","Chicken Fried - Zac Brown Band","Wagon Wheel - Old Crow Medicine Show","Gunpowder & Lead - Miranda Lambert","Love Story - Taylor Swift","Our Song - Taylor Swift","Teardrops on My Guitar - Taylor Swift","Should've Been a Cowboy - Toby Keith","Courtesy of the Red, White and Blue - Toby Keith","Some Beach - Blake Shelton","God Gave Me You - Blake Shelton","Honey Bee - Blake Shelton","Boys 'Round Here - Blake Shelton","Ol' Red - Blake Shelton","Austin - Blake Shelton","The House That Built Me - Miranda Lambert","Over You - Miranda Lambert","Mama's Broken Heart - Miranda Lambert","Vice - Miranda Lambert","Bluebird - Miranda Lambert","Tin Man - Miranda Lambert","Automatic - Miranda Lambert",'Friends In Low Places - Garth Brooks', 'Jolene - Dolly Parton', 'Take Me Home, Country Roads - John Denver', 'Ring of Fire - Johnny Cash', 'I Walk The Line - Johnny Cash', 'Crazy - Patsy Cline', 'Your Cheatin Heart - Hank Williams', 'He Stopped Loving Her Today - George Jones', 'Coal Miners Daughter - Loretta Lynn', 'Mamas Dont Let Your Babies Grow Up to Be Cowboys - Waylon Jennings', 'Stand By Your Man - Tammy Wynette', 'The Gambler - Kenny Rogers', 'Always On My Mind - Willie Nelson', 'Folsom Prison Blues - Johnny Cash', 'I Fall to Pieces - Patsy Cline', 'Blue Moon of Kentucky - Bill Monroe', 'Wide Open Spaces - Dixie Chicks', 'Amazed - Lonestar', 'Chattahoochee - Alan Jackson', 'Where Were You (When the World Stopped Turning) - Alan Jackson', 'Live Like You Were Dying - Tim McGraw', 'Need You Now - Lady Antebellum', 'Before He Cheats - Carrie Underwood', 'My Front Porch Looking In - Lonestar', 'I Hope You Dance - Lee Ann Womack', 'Somebody Like You - Keith Urban', 'Chicken Fried - Zac Brown Band', 'Gunpowder & Lead - Miranda Lambert', 'I Run to You - Lady Antebellum', 'Love Story - Taylor Swift'],
    'disco': ['I Will Survive - Gloria Gaynor', 'Le Freak - Chic', 'Stayin Alive - Bee Gees', 'Super Freak - Rick James', 'Funky Town - Lipps Inc', 'Disco Inferno - Trammps', 'YMCA - Village People', 'Born To Be Alive - Patrick Hernandez', 'Billie Jean - Michael Jackson', 'Get Up…I Feel Like Being A Sex Machine - James Brown', 'Mandolay - La Flavour', 'I Feel Love - Donna Summer', 'Love To Love You Baby - Donna Summer', 'Shame - Evelyn Champagne King', 'I’m So Excited - Pointer Sisters', 'Do You Wanna Funk - Sylvester', 'Babe We’re Gonna Love Tonight - Lime', 'That’s The Way I Like It - K.C. & the Sunshine Band', 'Knock On Wood - Amii Stewart', 'Night Fever - Bee Gees', 'Last Dance - Donna Summer', 'Don\'t Leave Me This Way - Thelma Houston', 'Heaven Must Be Missing An Angel - Tavares', 'Take Your Time (Do It Right) - S.O.S. Band', 'Double Dutch Bus - Frankie Smith', 'Rapper\'s Delight - Sugarhill Gang', 'Feels Like I’m In Love - Kelly Marie', 'Celebration - Kool & the Gang', 'Don’t Stop Til You Get Enough - Michael Jackson', 'Love Hangover - Diana Ross', 'Hot Stuff - Donna Summer', 'Heaven Must Have Sent You - Bonnie Pointer', 'This Time Baby - Jackie Moore', 'Let’s All Chant - Michael Zager Band', 'Boogie Oogie Oogie - A Taste Of Honey', 'Get Down Tonight - K.C. & the Sunshine Band', 'Spank - Jimmy Bo Horne', 'Bad Girls - Donna Summer', 'The Hustle - Van McCoy', 'Ladies Night - Kool & the Gang', 'Macho Man - Village People', 'Turn The Beat Around - Vicki Sue Robinson', 'Never Can Say Goodbye - Gloria Gaynor', 'White Lines (Don’t Do It) - Grandmaster Flash', 'So Many Men, So Little Time - Miquel Brown', 'There But For The Grace Of God - Machine', 'The Love I Lost - Harold Melvin & Bluenotes', 'Come To Me - France Joli', 'I’ll Always Love My Mama - Intruders', 'Can’t Get Enough Of Your Love - Barry White', 'Bad Luck - Harold Melvin & Bluenotes''Stayin Alive - Bee Gees', 'Super Freak - Rick James', 'Le Freak - Chic', 'Dont Stop Til You Get Enough - Michael Jackson', 'I Will Survive - Gloria Gaynor', 'Funky Town - Lipps Inc', 'You Should Be Dancing - Bee Gees', 'Ring My Bell - Anita Ward', 'Kung Fu Fighting - Carl Douglas', 'Boogie Wonderland - Earth, Wind & Fire', 'YMCA - Village People', 'Dancing Queen - ABBA', 'Heart of Glass - Blondie', 'Night Fever - Bee Gees', 'Disco Inferno - The Trammps', 'I Feel Love - Donna Summer', 'Car Wash - Rose Royce', 'Shake Your Groove Thing - Peaches & Herb', 'You Make Me Feel (Mighty Real) - Sylvester', 'Hot Stuff - Donna Summer', 'Good Times - Chic', 'Upside Down - Diana Ross', 'Celebration - Kool & The Gang', 'Ain\'t No Stopping Us Now - McFadden & Whitehead', 'Don\'t Leave Me This Way - Thelma Houston', 'Love Rollercoaster - Ohio Players', 'Shake Your Booty - KC and the Sunshine Band', 'That\'s the Way (I Like It) - KC and the Sunshine Band', 'More Than a Woman - Tavares', 'Got to Be Real - Cheryl Lynn'],
    'hiphop': ["It Was a Good Day - Ice Cube","Juicy - The Notorious B.I.G.","N.Y. State of Mind - Nas","Dear Mama - 2Pac","Runaway - Kanye West","Alright - Kendrick Lamar","Stan - Eminem","Paid in Full - Eric B. & Rakim","C.R.E.A.M. - Wu-Tang Clan","Fight the Power - Public Enemy","Fuck tha Police - N.W.A","The Message - Grandmaster Flash & The Furious Five","Shook Ones, Pt. II - Mobb Deep","Rapper's Delight - The Sugarhill Gang","Lose Yourself - Eminem","99 Problems - Jay-Z","HUMBLE. - Kendrick Lamar","Passin' Me By - The Pharcyde","Gin and Juice - Snoop Dogg","They Reminisce Over You (T.R.O.Y.) - Pete Rock & C.L. Smooth","In Da Club - 50 Cent","Big Poppa - The Notorious B.I.G.","B.O.B - OutKast","Hard Knock Life (Ghetto Anthem) - Jay-Z","Can I Kick It? - A Tribe Called Quest","Nuthin' but a 'G' Thang - Dr. Dre","Empire State of Mind - Jay-Z","I Used to Love H.E.R. - Common","Regulate - Warren G","U.N.I.T.Y. - Queen Latifah","Doo Wop (That Thing) - Lauryn Hill","My Name Is - Eminem","The World Is Yours - Nas","Get Ur Freak On - Missy Elliott","Rosa Parks - OutKast","California Love - 2Pac","Planet Rock - Afrika Bambaataa","Straight Outta Compton - N.W.A","Hypnotize - The Notorious B.I.G.","Ms. Jackson - OutKast","The Real Slim Shady - Eminem","Gold Digger - Kanye West","Drop It Like It's Hot - Snoop Dogg","Hey Ya! - OutKast","Stronger - Kanye West","Crazy in Love - Beyoncé","Umbrella - Rihanna","Super Bass - Nicki Minaj","See You Again - Wiz Khalifa",'Juice - Notorious B.I.G.', 'Nuthin but a G Thang - Dr. Dre', 'Fight The Power - Public Enemy', 'Rappers Delight - Sugarhill Gang', 'The Message - Grandmaster Flash and the Furious Five', 'Planet Rock - Afrika Bambaataa', 'Straight Outta Compton - N.W.A', 'Stan - Eminem', 'California Love - 2Pac', 'C.R.E.A.M. - Wu Tang Clan', 'My Name Is - Eminem', 'In Da Club - 50 Cent', 'Hypnotize - Notorious B.I.G.', 'Gin and Juice - Snoop Dogg', 'Hard Knock Life - Jay-Z', 'Get Ur Freak On - Missy Elliott', 'U Can\'t Touch This - MC Hammer', 'Hot in Herre - Nelly', 'Ms. Jackson - Outkast', 'The Real Slim Shady - Eminem', 'Empire State of Mind - Jay-Z', 'Gold Digger - Kanye West', 'Drop It Like It\'s Hot - Snoop Dogg', 'Hey Ya! - Outkast', 'Lose Yourself - Eminem', 'Stronger - Kanye West', 'Crazy in Love - Beyonce', 'Umbrella - Rihanna', 'Super Bass - Nicki Minaj', 'See You Again - Wiz Khalifa'],
    'jazz': ["Freddie Freeloader - Miles Davis","Blue Train - John Coltrane","St. Thomas - Sonny Rollins","Mercy, Mercy, Mercy - Cannonball Adderley","Song for My Father - Horace Silver","Waltz for Debby - Bill Evans","West End Blues - Louis Armstrong","Giant Steps - John Coltrane","Desafinado - Stan Getz & Charlie Byrd","Night in Tunisia - Dizzy Gillespie","April in Paris - Count Basie","Misty - Erroll Garner","Take the 'A' Train - Duke Ellington","My Funny Valentine - Chet Baker","Round Midnight - Thelonious Monk","At Last - Etta James","Black Coffee - Peggy Lee","Satin Doll - Duke Ellington","Fly Me to the Moon - Frank Sinatra","Feeling Good - Nina Simone","Take Five - Dave Brubeck","So What - Miles Davis","Sing, Sing, Sing - Benny Goodman","Strange Fruit - Billie Holiday","A Love Supreme, Part 1: Acknowledgement - John Coltrane","In a Sentimental Mood - Duke Ellington, John Coltrane","Birdland - Weather Report","Mack the Knife - Ella Fitzgerald","Body and Soul - Coleman Hawkins","Blue Rondo a la Turk - Dave Brubeck","God Bless The Child - Billie Holiday","Summertime - George Gershwin","What a Wonderful World - Louis Armstrong","Lush Life - Billy Strayhorn","Maiden Voyage - Herbie Hancock","Blue in Green - Miles Davis","The Girl From Ipanema - Antônio Carlos Jobim","Watermelon Man - Herbie Hancock","Cantaloupe Island - Herbie Hancock","Chameleon - Herbie Hancock","Breezin - George Benson","Moanin - Art Blakey & The Jazz Messengers","Goodbye Pork Pie Hat - Charles Mingus","Spain - Chick Corea","Autumn Leaves - Cannonball Adderley","Sidewinder - Lee Morgan","Stolen Moments - Oliver Nelson","I Loves You Porgy - Nina Simone","The In Crowd - Ramsey Lewis","The Sidewinder - Lee Morgan",'So What - Miles Davis', 'Take Five - Dave Brubeck', 'My Favorite Things - John Coltrane', 'A Love Supreme - John Coltrane', 'Birdland - Weather Report', 'Round Midnight - Thelonious Monk', 'Mack the Knife - Ella Fitzgerald', 'Take The A Train - Duke Ellington', 'Body and Soul - Coleman Hawkins', 'Blue Rondo a la Turk - Dave Brubeck', 'In a Sentimental Mood - Duke Ellington', 'God Bless The Child - Billie Holiday', 'Strange Fruit - Billie Holiday', 'Summertime - George Gershwin', 'What a Wonderful World - Louis Armstrong', 'My Funny Valentine - Chet Baker', 'Lush Life - Billy Strayhorn', 'Maiden Voyage - Herbie Hancock', 'Blue in Green - Miles Davis', 'The Girl From Ipanema - Antônio Carlos Jobim', 'Watermelon Man - Herbie Hancock', 'Cantaloupe Island - Herbie Hancock', 'Chameleon - Herbie Hancock', 'Breezin - George Benson', 'Moanin - Art Blakey & The Jazz Messengers', 'Goodbye Pork Pie Hat - Charles Mingus', 'Spain - Chick Corea', 'Autumn Leaves - Cannonball Adderley', 'Waltz for Debby - Bill Evans', 'Sidewinder - Lee Morgan'],
    'metal': ["Hells Bells - AC/DC","For Whom The Bell Tolls - Metallica","Children Of The Grave - Black Sabbath","Electric Eye - Judas Priest","The Last In Line - Dio","Peace Sells - Megadeth","South Of Heaven - Slayer","Cowboys From Hell - Pantera","Hangar 18 - Megadeth","Caught Somewhere In Time - Iron Maiden","Holy Wars... The Punishment Due - Megadeth","Aces High - Iron Maiden","Rust in Peace... Polaris - Megadeth","2 Minutes To Midnight - Iron Maiden","The Clairvoyant - Iron Maiden","Seasons In The Abyss - Slayer","Ride The Lightning - Metallica","Indians - Anthrax","Among The Living - Anthrax","Be All, End All - Anthrax","Madhouse - Anthrax","I Am The Law - Anthrax","Got The Time - Anthrax","Antisocial - Anthrax","Bring The Noise - Anthrax","In My Darkest Hour - Megadeth","Tornado Of Souls - Megadeth","Lucretia - Megadeth","Five Magics - Megadeth","Poison Was The Cure - Megadeth","Killing Is My Business... And Business Is Good! - Megadeth","Mechanix - Megadeth","Wake Up Dead - Megadeth","The Conjuring - Megadeth","Devil's Island - Megadeth","Good Mourning / Black Friday - Megadeth","Bad Omen - Megadeth","I Ain't Superstitious - Megadeth","My Last Words - Megadeth","Skin O' My Teeth - Megadeth","Symphony Of Destruction - Megadeth","Architecture Of Aggression - Megadeth","Foreclosure Of A Dream - Megadeth","Sweating Bullets - Megadeth","This Was My Life - Megadeth","Countdown To Extinction - Megadeth","High Speed Dirt - Megadeth","Psychotron - Megadeth","Captive Honour - Megadeth","Ashes In Your Mouth - Megadeth","Enter Sandman - Metallica","Iron Man - Black Sabbath","Master Of Puppets - Metallica","Paranoid - Black Sabbath","The Number Of The Beast - Iron Maiden","War Pigs - Black Sabbath","Back In Black - AC/DC","Breaking The Law - Judas Priest","Crazy Train - Ozzy Osbourne","Raining Blood - Slayer","Fear Of The Dark - Iron Maiden","Ace Of Spades - Motörhead","Painkiller - Judas Priest","One - Metallica","Bark At The Moon - Ozzy Osbourne","Chop Suey! - System Of A Down","Walk - Pantera","Cowboys From Hell - Pantera","Run To The Hills - Iron Maiden","Hallowed Be Thy Name - Iron Maiden","Blackened - Metallica","Holy Diver - Dio","Angel Of Death - Slayer","Symphony Of Destruction - Megadeth","Fade To Black - Metallica","Welcome To The Jungle - Guns N' Roses","Sweet Child O' Mine - Guns N' Roses","Pull Me Under - Dream Theater","Stargazer - Rainbow","The Trooper - Iron Maiden"],
    'pop': ['Let\'s Dance - David Bowie', 'Careless Whisper - George Michael', 'Sweet Child o\' Mine - Guns N\' Roses', 'Take My Breath Away - Berlin', 'Livin\' on a Prayer - Bon Jovi', 'Don\'t Stop Believin\' - Journey', 'I Want to Know What Love Is - Foreigner', 'Africa - Toto', 'Under Pressure - Queen and David Bowie', 'Every Breath You Take - The Police', 'Back in Black - AC/DC', 'Call Me - Blondie', 'Beat It - Michael Jackson', 'Bette Davis Eyes - Kim Carnes', 'Start Me Up - The Rolling Stones', 'Down Under - Men at Work', 'Endless Love - Diana Ross and Lionel Richie', 'Lady - Kenny Rogers', 'Centerfold - The J. Geils Band', 'Eye of the Tiger - Survivor''Thriller - Michael Jackson', 'Like a Prayer - Madonna', 'Billie Jean - Michael Jackson', 'When Doves Cry - Prince', 'I Wanna Dance with Somebody - Whitney Houston', 'Every Breath You Take - The Police', 'Superstition - Stevie Wonder', 'What A Feeling - Irene Cara', 'Like A Virgin - Madonna', 'Bad - Michael Jackson', 'Material Girl - Madonna', 'Beat It - Michael Jackson', 'Sweet Dreams (Are Made of This) - Eurythmics', 'Call Me - Blondie', 'Karma Chameleon - Culture Club', 'Tainted Love - Soft Cell', 'Take On Me - a-ha', 'Don\'t You Want Me - The Human League', 'Girls Just Want to Have Fun - Cyndi Lauper', 'Wake Me Up Before You Go-Go - Wham!', 'You Spin Me Round (Like a Record) - Dead or Alive', 'Never Gonna Give You Up - Rick Astley', 'I\'m So Excited - The Pointer Sisters', 'Footloose - Kenny Loggins', 'Uptown Girl - Billy Joel', 'Don\'t Stop Believin\' - Journey', 'Time After Time - Cyndi Lauper', 'Eye of the Tiger - Survivor', 'Physical - Olivia Newton-John', 'Flashdance... What a Feeling - Irene Cara'],
    'reggae': ['No Woman, No Cry - Bob Marley', 'Redemption Song - Bob Marley', 'One Love - Bob Marley', 'The Harder They Come - Jimmy Cliff', 'Legalize It - Peter Tosh', 'Marcus Garvey - Burning Spear', 'Here I Come - Barrington Levy', 'A Love I Can Feel - John Holt', '54-46 Was My Number - Toots & the Maytals', 'Police & Thieves - Junior Murvin', 'War Ina Babylon - Max Romeo', 'Two Sevens Clash - Culture', 'Guess Who\'s Coming to Dinner - Black Uhuru', 'Sponji Reggae - Black Uhuru', 'Funky Kingston - Toots & The Maytals', 'Pass The Kutchie - Mighty Diamonds', 'Stir It Up - Bob Marley', 'Israelites - Desmond Dekker & The Aces', 'Tomorrow People - Ziggy Marley', 'Rivers of Babylon - The Melodians', 'Sun Is Shining - Bob Marley', 'Night Nurse - Gregory Isaacs', 'Angel - Shaggy', 'Kingston Town - UB40', 'Bad Boys - Inner Circle', 'Sweat (A La La La La Long) - Inner Circle', 'Boom Shack-A-Lak - Apache Indian', 'It Wasn\'t Me - Shaggy', 'Red Red Wine - UB40', 'Three Little Birds - Bob Marley'],
    'rock': ['Stairway to Heaven - Led Zeppelin', 'Bohemian Rhapsody - Queen', 'Hotel California - The Eagles', 'Like a Rolling Stone - Bob Dylan', 'Imagine - John Lennon', 'Smells Like Teen Spirit - Nirvana', 'Hey Jude - The Beatles', 'Sweet Child O Mine - Guns N Roses', 'Born to Run - Bruce Springsteen', 'Comfortably Numb - Pink Floyd', 'Another Brick In The Wall - Pink Floyd', 'Livin On A Prayer - Bon Jovi', 'Light My Fire - The Doors', 'You Shook Me All Night Long - AC/DC', 'More Than a Feeling - Boston', 'Black Dog - Led Zeppelin', 'Go Your Own Way - Fleetwood Mac', 'We Will Rock You - Queen', 'Under Pressure - Queen', 'Baba O\'Riley - The Who', 'Back In Black - AC/DC', 'Money - Pink Floyd', 'Wish You Were Here - Pink Floyd', 'Free Bird - Lynyrd Skynyrd', 'Don\'t Stop Believin\' - Journey', 'American Pie - Don McLean', 'All Along The Watchtower - Jimi Hendrix', 'Tom Sawyer - Rush', 'With Or Without You - U2', 'Dream On - Aerosmith']
    }
    # Check if the genre exists in the dictionary
    # if genre in songs:
        # If the genre exists, return 10 random songs from the genre
    return random.sample(songs[genre], 10)


def getmetadata(y,sr):
    # import librosa
    # y, sr = librosa.load(song, mono=True, duration=500)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    feature_dict = {
        
        'chroma_stft_mean': np.mean(chroma_stft),
        'chroma_stft_var': np.var(chroma_stft),
        'rms_mean': np.mean(rms),
        'rms_var': np.var(rms),
        'spectral_centroid_mean': np.mean(spec_cent),
        'spectral_centroid_var': np.var(spec_cent),
        'spectral_bandwidth_mean': np.mean(spec_bw),
        'spectral_bandwidth_var': np.var(spec_bw),
        'rolloff_mean': np.mean(rolloff),
        'rolloff_var': np.var(rolloff),
        'zero_crossing_rate_mean': np.mean(zcr),
        'zero_crossing_rate_var': np.var(zcr),
        # 'harmony_mean': ..., # Not standard, requires additional context.
        # 'harmony_var': ..., # Not standard, requires additional context.
        # 'perceptr_mean': ..., # Not standard, requires additional context.
        # 'perceptr_var': ..., # Not standard, requires additional context.
        'tempo': librosa.feature.tempo(y=y, sr=sr)[0],
        
    }
    
    for i in range(1, 21): # For each of 20 MFCCs
        feature_dict[f'mfcc{i}_mean'] = np.mean(mfcc[i-1])
        feature_dict[f'mfcc{i}_var'] = np.var(mfcc[i-1])
    # 'label': ... # Requires additional context. 
    return list(feature_dict.values())

st.set_page_config(page_title='Music Genre Prediction', layout="centered", initial_sidebar_state="collapsed",

                   page_icon="icon.jpeg",
                   menu_items={
                       'Get Help': 'https://github.com/regnna',
                       'Report a bug': 'https://github.com/regnna',
                       'About': 'Regnna'
                   })
utl.local_css("frontend/css/streamlit.css")
# utl.remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

st.markdown("<h1 style='text-align: center; color: gold;'> Find Your Music Genres </h1>",
            unsafe_allow_html=True)

hide_st_style = """
                <style>
                header{visibility:hidden;}
                footer{visibility:hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Add background image

st.markdown(
    f"""
         <style>
         .stApp {{
             background-image:
              url("https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)


with st.expander("Description"):
    st.info("""A Simple ML Website to predict genre of a given music/song, the .wav file of the audio required to detect its genre.
    ENJOY!!
 """)
uploaded_file = st.file_uploader("Upload a .wav file please", type='wav')

if uploaded_file is None:
    st.write("Please upload a WAV file.")

else:
    # Process the uploaded WAV file
    import librosa
    y, sr = librosa.load(uploaded_file, mono=True, duration=500)
    st.audio(y, sample_rate=sr)

    g = getmetadata(y,sr)
    path = os.path.join('svc_model (2).hdf5')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    svmp = data['svmp']
    norma = data['norma']
    lgn = data['lgn']
    x = norma.transform([g])
    pred = svmp.predict(x)
    st.markdown(f"<h3 style='text-align: center; color: white;'> {pred[0]} </h3>",
                unsafe_allow_html=True)
    lst=get_songs(pred[0])
    #  lst = ['a', 'b', 'c'] 
    # print(lst)
    s = ''
    
    for i in lst:
        s +="- "+i + "\n"
    
    my_expander = st.expander(label='Recommended Playlist')
    # my_expander=st.expander(label=st.markdown(f"<h4 style='text-align: center; color: gold;'> Recommended Playlist </h4>",
                # unsafe_allow_html=True))
    # with stylable_container()
    
        
    with my_expander:
            with stylable_container(
                key='custom_expand',
                css_styles="""
                {
                        color: gold;
                        text-align: center;
                        text:bold;
                    }
                    """,

            ):
            # st.markdown(f"<h4 style='text-align: center; color: gold;'> Recommended Playlist </h4>",
            #         unsafe_allow_html=True)
                # st.markdown(f"<h3 style='text-align: center; color: gold;'>{s}</h3>\n",unsafe_allow_html=True)
                st.markdown(s)
    
    # st.markdown(f"<h5 style='text-align: center; color: white;'> {t} </h5>",unsafe_allow_html=True)
    # s = '' 
    # for i in lst:
    # 
        # st.markdown("-"+f"<h5 style='text-align: center; color: white;'> {i} </h5>",unsafe_allow_html=True)
        # s += " " + i + "\n"
    # st.markdown(
    #     """
    # # f"<h3 style='text-align: center; color: white;'> {s} </h3>",
    # <style>
    # [data-testid="stMarkdownContainer"] ul{
    # list-style-position: inside;
    # }
    # </style>""",
    #             unsafe_allow_html=True)

    # st.write(pred[0])
