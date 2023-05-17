const f1 = (s) => {
    /**
     * 搜索题中括号算式
     * Author: J.sky
     * Mail: bosichong@qq.com
     * @param {string} s 算式
     * @return {string} 搜索括号算式
     */
    const ss = s.match(/\(\d+[\+\-\*/\d]+\)/);
    if (ss) {
        return ss[0];
    }
    return null;
};

const f2 = (s) => {
    /**
     * 搜索题中乘除法算式
     * Author: J.sky
     * Mail: bosichong@qq.com
     * @param {string} s 算式
     * @return {string} 乘除法算式
     */
    const ss = s.match(/\d+[\*/]\d+/);
    if (ss) {
        return ss[0];
    }
    return null;
};

const f3 = (s) => {
    /**
     * 搜索加减法算式
     * Author: J.sky
     * Mail: bosichong@qq.com
     * @param {string} s 算式
     * @return {string} 加减法算式
     */
    const ss = s.match(/\d+[\+\-]\d+/);
    if (ss) {
        return ss[0];
    }
    return null;
};

const f4 = (s) => {
    /**
     * 搜索加减法乘除算式
     * Author: J.sky
     * Mail: bosichong@qq.com
     * @param {string} s 算式
     * @return {string} 加减乘除算式
     */
    const ss = s.match(/\d+[\+\-\*/\d]+/);
    if (ss) {
        return ss[0];
    }
    return null;
};


/**
 * 算式分解校验器
 * Author: J.sky
 * Mail: bosichong@qq.com
 * @param {string} s 算式
 * @param {number} result 算式结果
 * @param {number} carry 进位
 * @param {number} abdication 借位
 * @param {number} remainder 余数
 * @return {boolean}
 */
function validator(s, result, carry, abdication, remainder) {
    if (isResultOk(s, result)) {
        if (f1(s)) {
            s = validator1(s, result, carry, abdication, remainder);
            if (s) {
                return validator2(s, result, carry, abdication, remainder);
            } else {
                return false;
            }
        } else {
            return validator2(s, result, carry, abdication, remainder);
        }
    } else {
        return false;
    }
}

/**
 * 算式分解校验器提取括号内算式，然后递归给validator2进行算式验证
 * 本方法可以递归提取括号嵌套算式
 * Author: J.sky
 * Mail: bosichong@qq.com
 * @param {string} s 算式
 * @param {number} result 算式结果
 * @param {number} carry 进位
 * @param {number} abdication 借位
 * @param {number} remainder 余数
 * @return {boolean}
 */
function validator1(s, result, carry, abdication, remainder) {
    while (f1(s)) {
        const fa = f1(s);
        const fb = f4(f1(s));
        const r = validator2(fb, result, carry, abdication, remainder);
        if (r) {
            s = s.replace(fa, `${parseInt(parseFloat(r))}`);
        } else {
            return false;
        }
    }
    return s;
}

/**
 * 分解乘除加减法计算结果并校验
 * Author: J.sky
 * Mail: bosichong@qq.com
 * @param {string} s 算式
 * @param {number} result 算式结果
 * @param {number} carry 进位
 * @param {number} abdication 借位
 * @param {number} remainder 余数
 * @return {boolean}
 */
function validator2(s, result, carry, abdication, remainder) {
    // 乘除法验证
    while (f2(s)) {
        const f = f2(s);
        if (isMultDivOk(f, result, remainder)) {
            const r = eval(f);
            s = s.replace(f, `${parseInt(parseFloat(r))}`);
        } else {
            return false;
        }
    }
    // 加减法验证
    while (f3(s)) {
        const f = f3(s);
        if (isAddSub(f, result, carry, abdication)) {
            const r = eval(f);
            s = s.replace(f, `${r}`);
        } else {
            return false;
        }
    }
    return s;
}


/**
 * 验证算式结果是否正确
 *
 * Author  : J.sky
 * Mail    : bosichong@qq.com
 * @param {string} str 一道算式题
 * @param {Array} result 结果范围
 * @return {boolean}
 */
const isResultOk = (str, result) => {
    try {
        return result[0] <= eval(str) && eval(str) <= result[1];
    } catch (e) {
        return false;
    }
};


const isMultDivOk = (s, result, remainder) => {
    /**
     * 判断乘除法正确性
     * @param {string} s 算式
     * @param {Array} result 结果范围
     * @param {number} remainder 余数
     * @return {boolean}
     */
    if (s.includes("/")) {
        const divs = s.split("/");
        if (parseInt(divs[1]) === 0) {
            return false;
        } else {
            // 除法，除数不能为0，并且结果在范围内,并且整除无余数
            if (remainder === 2) {
                if (
                    isResultOk(s, result) &&
                    parseInt(divs[0]) % parseInt(divs[1]) === 0 &&
                    eval(s) > 0
                ) {
                    return true;
                } else {
                    return false;
                }
            }
            if (remainder === 3) {
                if (
                    isResultOk(s, result) &&
                    parseInt(divs[0]) % parseInt(divs[1]) > 0 &&
                    eval(s) > 0
                ) {
                    return true;
                } else {
                    return false;
                }
            } else if (remainder === 1) {
                if (isResultOk(s, result) && eval(s) > 0) {
                    return true;
                } else {
                    return false;
                }
            }
        }
    }

    if (s.includes("*")) {
        return isResultOk(s, result); // 乘法结果在范围内
    }
};


const isAddSub = (s, result, carry, abdication) => {
    /**
     * 判断加减法正确性
     * @param {string} s 算式
     * @param {Array} result 结果范围
     * @param {number} carry 进位
     * @param {number} abdication 退位
     * @return {boolean}
     */
    const tmp = s.split(/[+\-]/);
    if (isResultOk(s, result)) {
        if (/\+/.test(s)) {
            if (carry === 1) {
                return true;
            } else if (carry === 2) {
                return is_addcarry(parseInt(tmp[0]), parseInt(tmp[1]));
            } else if (carry === 3) {
                return is_addnocarry(parseInt(tmp[0]), parseInt(tmp[1]));
            }
        } else if (/\-/.test(s)) {
            if (abdication === 1) {
                return true;
            } else if (abdication === 2) {
                return is_abdication(parseInt(tmp[0]), parseInt(tmp[1]));
            } else if (abdication === 3) {
                return is_noabdication(parseInt(tmp[0]), parseInt(tmp[1]));
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
};

const getMoreStep = (formulas, result, symbols, step, carry, abdication, remainder, is_bracket, is_result) => {
    /**
     * 生成符合规则的口算运算题
     * @param {Array} formulas 整数算数项
     * @param {Array} result 最终结果范围
     * @param {Array} symbols 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
     * @param {number} step 步数
     * @param {number} carry 加法是否进位
     * @param {number} abdication 减法是否退位
     * @param {number} remainder 除法余数
     * @param {number} is_bracket 是否包含括号
     * @param {number} is_result 求结果，求运算项
     * @return {string} 一道符合规则的口算运算题
     */
    const f = getRandomNum(formulas, step);
    const question = getPSMstr(f, symbols, step, is_bracket);

    if (validator(question, result, carry, abdication, remainder)) {
        return getXStepstr(question, is_result);
    } else {
        return false;
    }
};


function getPSMstr(formulas, symbols, step, is_bracket) {
    /**
     * 生成算式题
     * @param {Array} formulas 给定的算数项列表
     * @param {Array} symbols 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
     * @param {number} step 步数
     * @param {number} is_bracket 括号
     * @return {string}
     */
    let ss = "";
    const sym = getRandomSymbols(symbols, step);
    for (let i = 0; i < step; i++) {
        formulas.splice(i * 2 + 1, 0, getSymbol(sym[i]));
    }

    if (is_bracket) {
        const k = getRandomBracket(step); // 获得一个括号起始指针
        for (let i = 0; i < 2; i++) {
            if (i === 0) {
                formulas.splice(k + 4 * i, 0, "(");
            } else {
                formulas.splice(k + 4 * i, 0, ")");
            }
        }
    }

    for (const s of formulas) {
        ss += s;
    }
    return ss;
}

function getRandomBracket(step) {
    /**
     * 返回一个括号起始随机数
     * @param {number} step
     * @return {number}
     */
    while (true) {
        const k = Math.floor(Math.random() * (step * 2 + 1 - 3)); // 获得一个括号起始指针
        if (k % 2 === 0) {
            return k;
        }
    }
}

// 2步算式相关判断设置

/**
 * 给定一组算式和其结果，根据条件生成求结果或是求算数项的题型
 * @param {string} src 算式
 * @param {number} is_result 0or1
 * @return {string}
 */
function getXStepstr(src, is_result) {
    if (is_result == 0) {
        return repSymStr(src) + "=";
    } else if (is_result == 1) {
        return getRandomItem(repSymStr(src) + "=" + eval(src));
    } else {
        throw new Error("is_result求结果，求算数项参数设置错误！");
    }
}


/**
 * 更换乘除法符号
 * @param {string} s
 * @return {string}
 */
function repSymStr(s) {
    if (/\*/.test(s)) {
        s = s.replace(/\*/g, "×");
    }
    if (/\//.test(s)) {
        s = s.replace(/\//g, "÷");
    }
    return s;
}


/**
 * 把得到的算式转变成求算数项口算题
 * @param {string} sr 一道算数题
 * @return {string}
 */
function getRandomItem(sr) {
    let p = /\d+/g;
    let sc = sr.match(p);
    let i = Math.floor(Math.random() * (sc.length - 1)); // -1防止替换结果
    sr = sr.replace(sc[i], "__");
    return sr;
}


/**
 * 获得运算符号，用来运算结果
 * @param {number} sym
 * @return {string}
 */
function getSymbol(sym) {
    if (sym == 1) {
        return "+";
    } else if (sym == 2) {
        return "-";
    } else if (sym == 3) {
        return "*";
    } else if (sym == 4) {
        return "/";
    }
}

/**
 * 返回一组运算符号
 * @param {Array} symbols 每步题的算数符号（例 [[1,2],[1,]]  第一个运算符可以为+或-，第二个运算符只能为+）
 * @param {number} step 运算步
 * @return {Array}
 */
function getRandomSymbols(symbols, step) {
    let newList = [];
    for (let i = 0; i < step; i++) {
        let index = Math.floor(Math.random() * symbols[i].length);
        newList.push(symbols[i][index]);
    }
    return newList;
}


/**
 * 判断加法进位
 * @param {number} a
 * @param {number} b
 * @return {boolean}
 */
function is_addcarry(a, b) {
    return (get_num(a) + get_num(b) > 10);
}

/**
 * 判断加法无进位
 * @param {number} a
 * @param {number} b
 * @return {boolean}
 */
function is_addnocarry(a, b) {
    return !is_addcarry(a, b);
}

/**
 * 判断减法退位
 * @param {number} a
 * @param {number} b
 * @return {boolean}
 */
function is_abdication(a, b) {
    if (get_num(a) < get_num(b)) {
        return true;
    } else {
        return false;
    }
}

/**
 * 判断减法无退位
 * @param {number} a
 * @param {number} b
 * @return {boolean}
 */
function is_noabdication(a, b) {
    return !is_abdication(a, b);
}

/**
 * 判断乘法和乘法是否存在进位
 * @param {number} a
 * @param {number} b
 * @return {boolean}
 */
function is_multcarry(a, b) {
    if (get_num(a) * get_num(b) < 10) {
        return false;
    } else {
        return true;
    }
}

/**
 * 判断一个数是否为整数
 * @param {number} num
 * @return {boolean}
 */
function is_int(num) {
    return Number.isInteger(num);
}

/**
 * 返回一个整数的个位数
 * @param {number} number
 * @return {number}
 */
function get_num(number) {
    let value0 = number / 10;
    value0 = parseInt(value0);
    return number - value0 * 10;
}

/**
 * 根据所给的数值范围，步数，返回合法的数值。
 * @param {Array} list
 * @param {number} step
 * @return {Array}
 */
function getRandomNum(list, step) {
    let newList = [];
    for (let i = 0; i < step + 1; i++) {
        newList.push(Math.floor(Math.random() * (list[i][1] - list[i][0] + 1) + list[i][0]));
    }
    return newList;
}

/**
 * 定义一个程序运行时间计算装饰器无返回结果
 * @param {function} func
 * @return {function}
 */
function get_time(func) {
    return function (...args) {
        let start = performance.now();
        func.apply(this, args);
        let end = performance.now();
        console.log(`程序运行时间:${end - start}ms`);
    };
}


export default class FormulasGenerator {
    /**
     * 口算题生器核心类，负责生成完整的口算题
     * @param {Object} addattrs
     * @param {Object} subattrs
     * @param {Object} multattrs
     * @param {Object} divattrs
     * @param {number} step
     * @param {number} number
     * @param {boolean} is_result
     * @param {boolean} is_bracket
     * @param {Array} multistep
     * @param {Array} symbols
     */
    constructor(addattrs, subattrs, multattrs, divattrs, step, number, is_result, is_bracket, multistep, symbols) {
        if (step === undefined) {
            throw new Error("required param signum is missing or signum is None");
        }
        if (![1, 2, 3].includes(step)) {
            throw new Error("param signum must be 1 or 2 or 3");
        }

        this.addattrs = addattrs;
        this.subattrs = subattrs;
        this.multattrs = multattrs;
        this.divattrs = divattrs;
        this.step = step;
        this.is_result = is_result;
        this.is_bracket = is_bracket;
        this.number = number;
        this.multistep = multistep;
        this.symbols = symbols;
        this.__data_list = [];  // 生成的口算题
    }

    /**
     * 根据给出的属性返回一道合法的口算题
     * @return {string} 一道合法的口算题
     */
    __getformula() {
        const f = this.__get_formulas();
        return getMoreStep(f, this.multistep[4], this.symbols, this.step, this.addattrs["carry"],
            this.subattrs["abdication"], this.divattrs["remainder"], this.is_bracket, this.is_result);
    }

    /**
     * 返回口算题算数项的取值范围list
     * @return {Array} 口算题算数项的取值范围list
     */
    __get_formulas() {
        const f = [];
        for (let i = 0; i < this.step + 1; i++) {
            f.push(this.multistep[i]);
        }
        return f;
    }

    /**
     * 根据条件生成所需口算题
     * @return {Array} 一组口算题
     */
    generate() {
        const slist = [];
        while (true) {
            const formula = this.__getformula();  // 生成一道算式题
            if (formula) {
                slist.push(formula);
            }
            if (slist.length === this.number) {
                break;
            }
        }

        slist.sort(() => Math.random() - 0.5);  // 洗牌，先打乱list中的排序
        this.__data_list = slist.slice(0, this.number);  // 随机取需要的口算题量。
        return this.__data_list;
    }
}


