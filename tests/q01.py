test = {
  'names': [
    'q01',
    '1',
    'q1'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> roll_dice(2, make_test_dice(4, 6, 1))
        56d669dcedf50b6144dee52c200c6a09
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> roll_dice(3, make_test_dice(4, 6, 1))
        6e5521930a0f3da01e4348a227cc686a
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> roll_dice(3, make_test_dice(1, 2, 3))
        6e5521930a0f3da01e4348a227cc686a
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> counted_dice = make_test_dice(4, 1, 2, 6)
        >>> roll_dice(3, counted_dice)
        6e5521930a0f3da01e4348a227cc686a
        # locked
        >>> roll_dice(1, counted_dice)  # Make sure you call dice exactly num_rolls times!
        859fd5e4a281547b44754134af76b8ac
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}