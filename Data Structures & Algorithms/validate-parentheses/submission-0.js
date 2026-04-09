class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];

    for (let i = 0; i <= s.length - 1; i++) {
        let char = s[i];
        if (char === '(' || char === '[' || char === '{') {
            stack.push(char);
        } else {
            let prevVal = stack.pop();

            if (prevVal === '(' && char !== ')') {
                return false;
            }
            if (prevVal === '[' && char !== ']') {
                return false;
            }
            if (prevVal === '{' && char !== '}') {
                return false;
            }
            if (prevVal === undefined) {
                return false;
            }
        }
    }

    return stack.length === 0;
    }
}
