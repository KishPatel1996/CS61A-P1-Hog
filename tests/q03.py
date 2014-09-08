test = {
  'names': [
    'q03',
    '3',
    'q3'
  ],
  'points': 1,
  'suites': [
    [
      {
        'locked': True,
        'test': """
        >>> select_dice(4, 24) == six_sided
        a76322f228d327b80b1d337dcea1b616
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(16, 64) == six_sided
        4c17a98808fc29fa97576a714812c3c6
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(0, 0) == six_sided
        a76322f228d327b80b1d337dcea1b616
        # locked
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': """
        >>> select_dice(50, 80) == six_sided
        4c17a98808fc29fa97576a714812c3c6
        # locked
        """,
        'type': 'doctest'
      }
    ]
  ]
}