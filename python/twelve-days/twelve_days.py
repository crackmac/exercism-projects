def recite(start_verse, end_verse):
    days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]
    gifts = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."
    ]
    
    result = []
    for verse in range(start_verse, end_verse+1):
        if verse == 1:
            start="On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
            result.append(start)
            break
        else:
            start="On the {} day of Christmas my true love gave to me: "
            opening_verse=start.format(days[verse-1])
            line=[opening_verse]
            line += gifts[(12-verse):]
            s = ""
            result.append(s.join(line))

    return(result)

    
# print(recite(4, 4))