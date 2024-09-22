import Foundation

class Task {
    var title: String
    var category: String
    var type: String
    var dueDate: Date?

    init(_ title: String, _ category: String, _ type: String, _ dueDate: Date?) {
        self.title = title
        self.category = category
        self.type = type
        self.dueDate = dueDate
    }
}

class TaskList {
    private var tasks: [Task] = []

    func addTask(_ task: Task) {
        tasks.append(task)
    }

    func printTasks() {
        for task in tasks {
            let dueDateString = task.dueDate != nil ? DateFormatter.localizedString(from: task.dueDate!, dateStyle: .medium, timeStyle: .none) : "no due date"
            print("[\(task.title) | \(task.category) | \(task.type) | \(dueDateString)]")
        }
    }

    func sortByDue() {
        tasks.sort { (task1, task2) -> Bool in
            if let dueDate1 = task1.dueDate, let dueDate2 = task2.dueDate {
                return dueDate1 < dueDate2
            } else if task1.dueDate != nil {
                return true
            } else {
                return false
            }
        }
    }

    func sortByCat() {
        tasks.sort { $0.category < $0.category }
    }
}

// Testing the code
var t1, t2, t3, t4: Task
let df = DateFormatter()
df.dateFormat = "dd-MMM-yyyy"
t1 = Task("Reg course", "ELEC3644", "Study", df.date(from: "20-Aug-2024"))
t2 = Task("Book ticket", "Mirror", "Event", df.date(from: "12-Oct-2024"))
t3 = Task("Learn driving", "Check availability", "Personal", nil)
t4 = Task("Attend seminar", "ChatGPT workshop", "Extracurricular", nil)

var tList = TaskList()
tList.addTask(t1)
tList.addTask(t2)
tList.addTask(t3)
tList.addTask(t4)

print("Initial Tasks")
tList.printTasks()

tList.sortByDue()
print("\nSort by Due Date")
tList.printTasks()

tList.sortByCat()
print("\nSort by Category")
tList.printTasks()
