public class Act2Runner {
    public static void main(String[] args) {
        System.out.println("Ethan Kuo is an in person student with a grade of 95.");
        System.out.println("Charles Li is a world campus student with a grade of 96.");
        In_Person inPersonStudent = new In_Person("Ethan", "Kuo", 95);
        World_Campus worldCampusStudent = new World_Campus("Charles", "Li", 96);
        System.out.println("\nEthan Kuo goes to class: ");
        inPersonStudent.attend_In_Person_Meeting();
        System.out.println("\nEthan Kuo goes to a zoom class: ");
        inPersonStudent.attend_Zoom_Meeting();
        System.out.println("\nCharles Li goes to a zoom class: ");
        worldCampusStudent.attend_Zoom_Meeting();
        System.out.println();
        inPersonStudent.get_grade();
        worldCampusStudent.get_grade();
    }
}
