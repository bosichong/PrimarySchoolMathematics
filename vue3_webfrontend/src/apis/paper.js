import request from '@/utils/request'


/**
 * 
 * @param {Object} options 
 * @param {Array} paperList 
 * @returns 
 */
export function generatePaper(options, paperList) {
  const postPaperList = paperList.map(p => {

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
      symbols
    }
  })

  const postOptions = {
    "juanzishu": options.numberOfPapers,
    "lieshu": options.numberOfPagerColumns,
    "docx": options.downloadPath,
    "jz_title": options.paperTitle,
    "inf_title": options.paperSubTitle,
    "solution": options.solution
  }

  console.log([postPaperList, postOptions]);

  return request.post(
    'api_producepsm', { data: JSON.stringify([postPaperList, postOptions]) })
}

/**
 * 
 * @returns 
 */
export function getDownloadLinksOfPapers() {
  return request.get('getpsmlist')
}

export async function loadConfiguration() {
  const { data: { config } } = await getConfiguration()
  const { docx: downloadPath } = config
  return { downloadPath }
}

export function getConfiguration() {
  return request.get('api_getconfigjson')
}