test = {
  'names': [
    'q04',
    '4',
    'q4'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(1, 1, goal=100) # start can be 0 or 1
        >>> score0
        bd1b2cf4c7a862e5e618a00f4c9cc69b
        # locked
        >>> score1
        bd1b2cf4c7a862e5e618a00f4c9cc69b
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(2, 7, goal=100)
        >>> score0
        625a374dc1f9b8422bddcfd42bc6571c
        # locked
        >>> score1
        56d669dcedf50b6144dee52c200c6a09
        # locked
        >>> start
        6e5521930a0f3da01e4348a227cc686a
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(8, 3, goal=100)
        >>> score0
        56d669dcedf50b6144dee52c200c6a09
        # locked
        >>> score1
        625a374dc1f9b8422bddcfd42bc6571c
        # locked
        >>> start
        625a374dc1f9b8422bddcfd42bc6571c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(4, 3, goal=100)
        >>> score0
        df6b7d0cff289551b96a353a6c64b996
        # locked
        >>> score1
        a4e96e54b9b170437d66dd7bd7e6c37c
        # locked
        >>> start
        625a374dc1f9b8422bddcfd42bc6571c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> score0, score1, start = bid_for_start(3, 4, goal=100)
        >>> score0
        a4e96e54b9b170437d66dd7bd7e6c37c
        # locked
        >>> score1
        df6b7d0cff289551b96a353a6c64b996
        # locked
        >>> start
        6e5521930a0f3da01e4348a227cc686a
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}