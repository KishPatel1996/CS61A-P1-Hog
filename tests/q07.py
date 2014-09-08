test = {
  'names': [
    'q07',
    '7',
    'q7'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(3)   # dice always returns 3
        >>> max_scoring_num_rolls(dice)
        56d669dcedf50b6144dee52c200c6a09
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'answer': '7ebcecfa5f29b7fa93c7df03331f65cb',
        'choices': [
          'The lowest num_rolls',
          'The highest num_rolls',
          'A random num_rolls'
        ],
        'locked': True,
        'question': """
        If multiple num_rolls are tied for the highest scoring
        average, which should you return?
        """,
        'type': 'concept'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(2)     # dice always rolls 2
        >>> max_scoring_num_rolls(dice)
        56d669dcedf50b6144dee52c200c6a09
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
        >>> max_scoring_num_rolls(dice)
        6e5521930a0f3da01e4348a227cc686a
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}