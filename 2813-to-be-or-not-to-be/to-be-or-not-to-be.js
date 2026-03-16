/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (arg) => arg === val ? true : (() => { throw new Error("Not Equal") })(),
        notToBe: (arg) => arg !== val ? true : (() => { throw new Error("Equal") })()
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */