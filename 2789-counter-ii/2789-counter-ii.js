/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init;

 const inc = () => ++count;
    function dec(){
        return --count;
    }
    function res(){
        count = init;
        return count;
    }
    return{
        increment: inc,
        decrement: dec,
        reset: res,
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */