/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {

        if (root == nullptr)
            return 0;

        // Current value is smaller than the range.
        // Left subtree will also be too small.
        if (root->val < low) {
            return rangeSumBST(root->right, low, high);
        }

        // Current value is larger than the range.
        // Right subtree will also be too large.
        if (root->val > high) {
            return rangeSumBST(root->left, low, high);
        }

        // Current value is inside [low, high]
        return root->val
             + rangeSumBST(root->left, low, high)
             + rangeSumBST(root->right, low, high);
    }
};