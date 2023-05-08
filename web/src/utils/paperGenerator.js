import FormulasGenerator from "./psm";

/**
 * 生成试卷
 * @param {Object} options 生成试卷的配置参数
 * @param {Array} paperList 需要生成的题型组
 * @returns
 */
export function createFormulasGenerator(options, paperList) {
  // 组装需要自动生成的题型组
  const postAutoGeneratePaperList = paperList.filter(p => !p.customFormulaList).map(p => {

    const multiSteps = p.formulaList.map(j => [parseInt(j.min), parseInt(j.max)])
    const symbols = p.formulaList.reduce((pre, cur) => {
      cur.operators && pre.push(cur.operators)
      return pre
    }, [])

    // 补缺
    for (let i = 0; i < 4 - p.formulaList.length; i++) {
      multiSteps.push([1, 9])
      symbols.push([1])
    }

    multiSteps.push([p.resultMinValue, p.resultMaxValue])

    return {
      step: parseInt(p.step),
      number: parseInt(p.numberOfFormulas),
      is_result: parseInt(p.whereIsResult),
      is_bracket: options.enableBrackets ? 1 : 0,
      add: { carry: parseInt(options.carry) },
      sub: { abdication: parseInt(options.abdication) },
      mult: {},
      div: { remainder: parseInt(options.remainder) },
      multistep: multiSteps,
      symbols,
    }
  })

  const papers = []

  for (let i = 0; i < parseInt(options.numberOfPapers); i++) {
    const f = postAutoGeneratePaperList.reduce((pre, cur) => {
      const op = cur
      const Gen = new FormulasGenerator(op.add, op.sub, op.mult, op.div, op.step, op.number, op.is_result, op.is_bracket, op.multistep, op.symbols)
      pre.push(...Gen.generate())
      return pre
    }, [])

    f.sort((pre, cur) => {
      return Math.random() > 0.5 ? -1 : 1
    })

    papers.push({
      paperTitle: options.paperTitle,
      paperSubTitle: options.paperSubTitle,
      numberOfPagerColumns: parseInt(options.numberOfPagerColumns),
      solution: options.solution,
      formulas: f
    })
  }

  console.log('papers', papers);
  return papers
}