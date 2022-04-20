import java.util.Scanner;
public class Exe1 
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        Double notas[] = new Double[10];
        Double medias[] = new Double[5];
        Double n1,n2,media;

        for(int i = 0; i < notas.length; i+=2)
        {
            System.out.println("Digite a 1a nota:");
            n1 = sc.nextDouble();
            while(n1 < 0 || n1 > 10)
            {
                System.out.println("Digite uma nota válida para a 1a nota:");
                n1 = sc.nextDouble();
            }
            
            System.out.println("Digite a 2a nota:");
            n2 = sc.nextDouble();
            while(n2 < 0 || n2 > 10)
            {
                System.out.println("Digite uma nota válida para a 2a nota:");
                n2 = sc.nextDouble();
            }
            notas[i] = n1;
            notas[i + 1] = n2;
        }

        for(int i = 0; i < notas.length; i+=2)
        {
            media = (notas[i]+notas[i+1])/2;
            medias[i/2] = media;
            System.out.println("A média do "+ ((i/2) + 1) + "o aluno é: " + media);
        }
    }
}