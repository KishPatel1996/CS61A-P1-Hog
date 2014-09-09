test = {
  'names': [
    'q00',
    '0',
    'q0'
  ],
  'points': 0,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> test_dice = make_test_dice(4, 1, 2)
        >>> test_dice()
        a4e96e54b9b170437d66dd7bd7e6c37c
        # locked
        >>> test_dice() # Second call
        6e5521930a0f3da01e4348a227cc686a
        # locked
        >>> test_dice() # Third call
        4024b7d247a7967fa973b60d80480da8
        # locked
        >>> test_dice() # Fourth call
        a4e96e54b9b170437d66dd7bd7e6c37c
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}