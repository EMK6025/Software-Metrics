public class World_Campus implements Grade, ZoomMeeting{
    String firstName = null;
    String lastName = null;
    int grade = -1;
    World_Campus(String first, String last, int curGrade){
        this.firstName = first;
        this.lastName = last;
        this.grade = curGrade;
    }
    public void get_grade() {
        System.out.println(this.firstName + " " + this.lastName + " has a grade of " + this.grade);
    }

    public void attend_Zoom_Meeting() {
        System.out.println(this.firstName + " " + this.lastName + " is now attending a Zoom meeting.");
    }
}
