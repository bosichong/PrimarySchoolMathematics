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

describe('FormulasGenerator.generate', () => {
  const createGenerator = (overrides = {}) => {
    const options = {
      addattrs: { carry: 1 },
      subattrs: { abdication: 1 },
      multattrs: {},
      divattrs: { remainder: 1 },
      step: 1,
      number: 10,
      is_result: 0,
      is_bracket: 0,
      multistep: [[1, 9], [1, 9], [1, 9], [1, 9], [1, 99]],
      symbols: [[1]],
      ...overrides
    }
    return new FormulasGenerator(
      options.addattrs,
      options.subattrs,
      options.multattrs,
      options.divattrs,
      options.step,
      options.number,
      options.is_result,
      options.is_bracket,
      options.multistep,
      options.symbols
    )
  }

  it('returns the requested number of formulas', () => {
    const gen = createGenerator({ number: 10 })
    expect(gen.generate()).toHaveLength(10)
  })

  it('returns non-empty string formulas', () => {
    const gen = createGenerator()
    const formulas = gen.generate()
    formulas.forEach(formula => {
      expect(typeof formula).toBe('string')
      expect(formula.length).toBeGreaterThan(0)
    })
  })

  it('appends equals sign when is_result is 0', () => {
    const gen = createGenerator({ is_result: 0 })
    const formulas = gen.generate()
    formulas.forEach(formula => {
      expect(formula.endsWith('=')).toBe(true)
    })
  })
})
