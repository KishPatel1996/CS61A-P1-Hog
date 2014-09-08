test = {
  'names': [
    'q09',
    '9',
    'q9'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(23, 60) # 23 + (1 + abs(6 - 0)) = 30
        625a374dc1f9b8422bddcfd42bc6571c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(27, 17) # 27 + (1 + abs(1 - 7)) = 34
        674201a6cd91521b7e90469728afef52
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(50, 80) # 1 + abs(8 - 0) = 9
        625a374dc1f9b8422bddcfd42bc6571c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(12, 12) # Baseline
        674201a6cd91521b7e90469728afef52
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'locked': True,
        'test': """
        >>> swap_strategy(15, 34, 5, 4) # beneficial swap
        625a374dc1f9b8422bddcfd42bc6571c
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> swap_strategy(8, 9, 5, 4) # harmful swap
        a4e96e54b9b170437d66dd7bd7e6c37c
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}