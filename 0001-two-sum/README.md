<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?


<div style="
  width: 50px;
  height: 50px;
  background: blue;
  animation: spin 2s linear infinite;
  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
">
</div>


<div style="
  animation: pulse 2s infinite;
  padding: 30px;
  background: linear-gradient(135deg, #6e8efb, #a777e3);
  border-radius: 16px;
  color: white;
  text-align: center;
  width: 320px;
  margin: 50px auto;
  box-shadow: 0 12px 36px rgba(0,0,0,0.2), 0 0 0 1px rgba(255,255,255,0.1);
  font-family: 'Segoe UI', system-ui, sans-serif;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-shadow: 0 2px 4px rgba(0,0,0,0.2);
">
  <div style="
    font-size: 18px;
    opacity: 0.9;
    margin-bottom: 8px;
    font-weight: 500;
  ">Awesome CSS Animation</div>
  <div style="
    font-size: 32px;
    font-weight: 800;
    margin: 10px 0;
  ">Pulse Effect!</div>
  <div style="
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 20px;
  ">
    <span style="
      display: inline-block;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: rgba(255,255,255,0.7);
      animation: pulse 1.5s infinite;
      animation-delay: 0s;
    "></span>
    <span style="
      display: inline-block;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: rgba(255,255,255,0.7);
      animation: pulse 1.5s infinite;
      animation-delay: 0.3s;
    ""></span>
    <span style="
      display: inline-block;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: rgba(255,255,255,0.7);
      animation: pulse 1.5s infinite;
      animation-delay: 0.6s;
    ""></span>
  </div>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
