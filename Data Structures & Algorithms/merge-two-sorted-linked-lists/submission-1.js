/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        const dummy = new ListNode(0);
        let prev = dummy;

        while (list1 && list2) {
            if (list1.val <= list2.val) {
                prev.next = list1;
                prev = list1;
                list1 = list1.next;
            } else {
                prev.next = list2;
                prev = list2;
                list2 = list2.next;
            }
        }
        if (list1 !== null) {
            prev.next = list1;
        } else if (list2 !== null) {
            prev.next = list2;
        }

        return dummy.next;
    }
}
