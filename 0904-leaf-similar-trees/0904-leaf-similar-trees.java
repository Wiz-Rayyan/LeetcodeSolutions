/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> ans1 = dfs(root1);
        List<Integer> ans2 = dfs(root2);
        return  Arrays.equals(ans1.toArray(),ans2.toArray()) ;
    }

    public List<Integer> dfs(TreeNode node) {
        Stack<TreeNode> s = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        Set<TreeNode> visited = new HashSet<>();

        s.add(node);
        while(!s.isEmpty()) {
            TreeNode n = s.pop();
            
            if(!visited.contains(n)) {
                visited.add(n);
                if(n.left == null && n.right == null) {
                    ans.add(n.val);
                }
                if(n.right != null) {
                    s.push(n.right);
                }
                if(n.left != null) {
                    s.push(n.left);
                }
                
                
            }


        }

        return ans;

    }
}