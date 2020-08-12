
/**
 * Problem: 1480. Running Sum of 1d Array
 * 
 * Given an array nums. We define a running sum of an array as 
 * runningSum[i] = sum(nums[0]…nums[i]). 
 * 
 * Return the running sum of nums.
 * 
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    sum = 0;
    arrr = [];
    for (i=0; i<nums.length; i++) {
        // do sumthing
        sum = sum + nums[i];
        arrr.push(sum);
    }
    return arrr;
    
};

nums = [1,2,3,4];
console.log(runningSum(nums));