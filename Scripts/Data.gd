class Company:
	var name: String
	var business_type: String
	var funds: int
	var rank: float
	var reputation: int

class WeeklyReport:
	var week: int
	var revenue: int
	var expenses: int
	var net_profit: int
	var rank_change: float
	var reputation_change: int

class RequestOpportunity:
	var id: String
	var title: String
	var description: String
	var client: String
	var time_estimate: int
	var payout: int
	var deadline: int


class BidOpportunity:
	var id: String
	var title: String
	var description: String
	var client: String
	var time_estimate: int
	var payout: int
	var deadline: int

class ServiceJob:
	var id: String
	var opportunity: RequestOpportunity
	var progress: float
	var time_spent: int
	var start_week: int
