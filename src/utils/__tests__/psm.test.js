import { describe, it, expect } from 'vitest'
import FormulasGenerator from '../psm.js'

describe('FormulasGenerator constructor', () => {
  const validArgs = [
    { carry: 1 }, // addattrs
    { abdication: 1 }, // subattrs
    {}, // multattrs
    { remainder: 1 }, // divattrs
    1, // step
    1, // number
    0, // is_result
    0, // is_bracket
    [[1, 9], [1, 9], [1, 99]], // multistep
    [[1]] // symbols
  ]

  it('throws when step is undefined', () => {
    const args = [...validArgs]
    args[4] = undefined
    expect(() => new FormulasGenerator(...args)).toThrow(
      'required param signum is missing or signum is None'
    )
  })

  it('throws when step is not 1, 2, or 3', () => {
    const args = [...validArgs]
    args[4] = 4
    expect(() => new FormulasGenerator(...args)).toThrow(
      'param signum must be 1 or 2 or 3'
    )
  })
})
