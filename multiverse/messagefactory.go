package multiverse

import (
	"sync/atomic"
	"time"
)

// region MessageFactory ///////////////////////////////////////////////////////////////////////////////////////////////

type MessageFactory struct {
	tangle         *Tangle
	sequenceNumber uint64
	numberOfNodes  uint64
}

func NewMessageFactory(tangle *Tangle, numberOfNodes uint64) (messageFactory *MessageFactory) {
	return &MessageFactory{
		tangle:        tangle,
		numberOfNodes: numberOfNodes,
	}
}

func (m *MessageFactory) CreateMessage(payload Color) (message *Message) {
	//strongParents, weakParents := m.tangle.TipManager.Tips()
	strongParents := m.tangle.TipManager.Tips()
	parentheight := 0
	// if strongParents.GetOne() != genesis {
	// 	parentheight = getmessage(strongParents.GetOne()).height
	// }
	var sp MessageID
	for s := range strongParents {
		sp = s
	}
	if sp != Genesis {
		if strongParents == nil {
			println("Strong Parent is nil")

		}
		if m.tangle.TipManager == nil {
			println("TipManager is nil")

		}
		msg, ok := m.tangle.TipManager.GetTip(sp)

		if ok {
			parentheight = msg
		}

	}

	return &Message{
		ID:            NewMessageID(),
		StrongParents: strongParents,
		//WeakParents:    weakParents,
		height:         parentheight + 1,
		SequenceNumber: atomic.AddUint64(&m.sequenceNumber, 1),
		Issuer:         m.tangle.Peer.ID,
		Payload:        payload,
		IssuanceTime:   time.Now(),
	}
}

// endregion ///////////////////////////////////////////////////////////////////////////////////////////////////////////
