"""Test data to test the parsing of the clipping data."""

# test_clipping_data.py

clipping_samples = [
    (
        (
            "Flowers For Algernon (S.F. MASTERWORKS) (Keyes, Daniel)\n"
            "- Your Highlight Location 1063-1064 | Added on Tuesday, 25 December 12 21:20:43\n\n"
            "Now I understand one of the important reasons for going to college and getting an education is to learn "
            "that the things you’ve believed in all your life aren’t true, and that nothing is what it appears to be."
            "\n==========\n"
        ),
        [{
            'book': 'Flowers For Algernon (S.F. MASTERWORKS)',
            'author': 'Keyes, Daniel',
            'location': '1063-1064',
            'date_added': 'Tuesday, 25 December 12 21:20:43',
            'clipping_text': ('Now I understand one of the important reasons for going to college and getting an '
                              'education is to learn that the things you’ve believed in all your life aren’t true, '
                              'and that nothing is what it appears to be.')
        }]
    ),
    (
        (
            "Thinking, Fast and Slow (Kahneman, Daniel)\n"
            "- Your Highlight on Page 54 | Location 926-927 | Added on Monday, 13 January 14 21:16:12\n\n"
            "You can see why the common admonition to “act calm and kind regardless of how you feel” is very good "
            "advice: you are likely to be rewarded by actually feeling calm and kind."
            "\n==========\n"
        ),
        [{
            'book': 'Thinking, Fast and Slow',
            'author': 'Kahneman, Daniel',
            'location': '926-927',
            'date_added': 'Monday, 13 January 14 21:16:12',
            'clipping_text': ('You can see why the common admonition to “act calm and kind regardless of how you feel” '
                              'is very good advice: you are likely to be rewarded by actually feeling calm and kind.')
        }]
    ),
    (
        (
            "The Norm Chronicles: Stories and numbers about danger (Blastland, Michael;Spiegelhalter, David)\n"
            "- Your Highlight Location 192-192 | Added on Tuesday, 11 June 13 13:36:36\n\n"
            "Probability is magical, a brilliant concept."
            "\n==========\n"
        ),
        [{
            'book': 'The Norm Chronicles: Stories and numbers about danger',
            'author': 'Blastland, Michael;Spiegelhalter, David',
            'location': '192-192',
            'date_added': 'Tuesday, 11 June 13 13:36:36',
            'clipping_text': 'Probability is magical, a brilliant concept.'
        }]
    ),
]

