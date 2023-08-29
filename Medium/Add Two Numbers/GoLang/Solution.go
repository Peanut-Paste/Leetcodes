func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// create a empty ListNode
	result := &ListNode{}
	// temp points to result so we will not traverse the original
	tmp := result
	for l1 != nil || l2 != nil {
		if l1 != nil {
			// not nil, add l1 val and move to next l1 node
			tmp.Val += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			// not nil, add l2 val and move to next l2 node
			tmp.Val += l2.Val
			l2 = l2.Next
		}
		// if current val is over 9
		if tmp.Val > 9 {
			// minus 10 and create new node having default value of 1
			tmp.Val -= 10
			tmp.Next = &ListNode{Val: 1}
			/* since we have shifted to next node above, we check if there's
			still nodes that is needed to create */
		} else if l1 != nil || l2 != nil {
			tmp.Next = &ListNode{}
		}
		tmp = tmp.Next
	}
	return result
}