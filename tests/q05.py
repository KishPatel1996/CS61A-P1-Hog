test = {
  'names': [
    'q05',
    '5',
    'q5'
  ],
  'params': {
    'doctest': {
      'cache': """
      always = hog.always_roll
      def weird_strat(score, opponent):
          return opponent // 10
      """,
      'setup': """
      hog.four_sided = make_test_dice(1)
      hog.six_sided = make_test_dice(3)
      """
    }
  },
  'points': 3,
  'suites': [
    [
      {
        'answer': 'a909b019025b11f3ba9f488f49085d48',
        'choices': [
          'While score0 and score1 are both less than goal',
          'While at least one of score0 or score1 is less than goal',
          'While score0 is less than goal',
          'While score1 is less than goal'
        ],
        'locked': True,
        'question': """
        The variables score0 and score1 are the scores for both
        players. Under what conditions should the game continue?
        """,
        'type': 'concept'
      },
      {
        'answer': 'aa7fad44ac47000ddd68fdce14423c3b',
        'choices': [
          'strategy1(score1, score0)',
          'strategy1(score0, score1)',
          'strategy1(score1)',
          'strategy1(score0)'
        ],
        'locked': True,
        'question': """
        If strategy1 is Player 1's strategy function, score0 is
        Player 0's current score, and score1 is Player 1's current
        score, then which of the following demonstrates correct
        usage of strategy1?
        """,
        'type': 'concept'
      },
      {
        'answer': 'a8103aff375e6d83da8988a7f69d7f28',
        'choices': [
          """
          After the current player takes her turn, and if either
          player's score is double the other player's score
          """,
          """
          After the current player takes her turn, and if the
          current player's score is double her opponent's score
          """,
          """
          Before the current player takes her turn, and if either
          player's score is double the other player's score
          """,
          """
          Before the current player takes her turn, and if the
          current player's score is double her opponent's score
          """
        ],
        'locked': True,
        'question': 'Recall the "swine swap" rule. When does this rule apply?',
        'type': 'concept'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(5), always(5))
        (92, 106)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(2), always(2))
        (17, 102)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(2), always(10))
        (19, 120)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(0), always(0))
        (101, 97)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(0), always(2))
        (100, 95)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(always(0), weird_strat)
        (64, 109)
        """,
        'type': 'doctest'
      },
      {
        'never_lock': True,
        'test': """
        >>> hog.play(weird_strat, weird_strat)
        (108, 93)
        """,
        'type': 'doctest'
      }
    ]
  ]
}