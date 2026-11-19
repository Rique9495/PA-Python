namespace main;

public class Program
{
    public static void Main(string[] args)
    {
        bool running = true;
        while(running)
        {
            Console.WriteLine("1 - Cadastre-se");
            Console.WriteLine("2 - Entre");
            Console.WriteLine("3 - Sair");
            Console.WriteLine("Aperte um número");

            ConsoleKeyInfo choose = Console.ReadKey();

            if (choose.Key == ConsoleKey.D1)
            {
                //Função que cria nova conta de D.S
            }
            else if (choose.Key == ConsoleKey.D2)
            {
                //Função que entra em uma conta
            }
            else if (choose.Key == ConsoleKey.D3)
            {
                //Saindo
                break;
            }
            else
            {
                Console.WriteLine("\nOpção errada!!!");
            }
        }
    }
}
//Classes
//Classe estudante
public class Student
{
    //privadas
    private string name = "";
    private int age;
    private int year;
    private string login = "";
    private string pwd = "";

    //publicas
    public string Name
    {
        get {return name;}
        set
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                Console.WriteLine("Valor inválido!!!");
            }
            else
            {
                name = value;
            }
        }
    }
    public string Login
    {
        get {return login;}
        set
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                Console.WriteLine("Valor inválido!!!");
            }
            else
            {
                login = value;
            }
        }
    }
    public string Pwd
    {
        get {return pwd;}
        set
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                Console.WriteLine("Valor inválido!!!");
            }
            else
            {
                pwd = value;
            }
        }
    }
    public int Year
    {
        get {return year;}
        set
        {
            if (year <= 0 || year > 3)
            {
                Console.WriteLine("Valor inválido!!!");
            }
            else
            {
                year = value;
            }
        }
    }
    public int Age
    {
        get {return age;}
        set
        {
            if (value <= 0 || value > 19)
            {
                Console.WriteLine("Valor inválido");
            }
            else
            {
                age = value;
            }
        }
    }

    //Constructor
    
}