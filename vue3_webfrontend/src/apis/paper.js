import request from '@/utils/request'


/**
 * 生成试卷
 * @param {Object} options 生成试卷的配置参数
 * @param {Array} paperList 需要生成的题型组
 * @returns 
 */
export function generatePaper(options, paperList) {
  // 组装需要自动生成的题型组
  const postAutoGeneratePaperList = paperList.filter(p => !p.customFormulaList).map(p => {

    const multiSteps = p.formulaList.map(j => [parseInt(j.min), parseInt(j.max)])
    multiSteps.push([p.resultMinValue, p.resultMaxValue])

    const symbols = p.formulaList.reduce((pre, cur) => {
      cur.operators && pre.push(cur.operators)
      return pre
    }, [])

    // 补缺
    for (let i = 0; i < 4 - p.formulaList.length; i++) {
      multiSteps.push([1, 9])
      symbols.push([1])
    }

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

  // 组装手动加入的题目
  const postCustomPaperList = paperList.filter(p => p.customFormulaList && p.customFormulaList.length).map(p => {
    return { ...p }
  })

  const postOptions = {
    "juanzishu": parseInt(options.numberOfPapers),
    "lieshu": parseInt(options.numberOfPagerColumns),
    "jz_title": options.paperTitle,
    "inf_title": options.paperSubTitle,
    "solution": options.solution,
    fileNameGeneratedRule: options.fileNameGeneratedRule
  }

  console.debug([postAutoGeneratePaperList, postOptions, postCustomPaperList])

  return request.post(
    'api/psm', { data: JSON.stringify([postAutoGeneratePaperList, postOptions, postCustomPaperList]) })
}