test = {
  'names': [
    'q02',
    '2',
    'q2'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> take_turn(2, 0,  make_test_dice(4, 6, 1))
        56d669dcedf50b6144dee52c200c6a09
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(3, 20, make_test_dice(4, 6, 1))
        6e5521930a0f3da01e4348a227cc686a
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 35)
        df6b7d0cff289551b96a353a6c64b996
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 71)
        4364babb02856efdee0f81d13fe70de0
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> take_turn(0, 7)
        25f3b898d8cf4f47d63a78f3b8237425
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}