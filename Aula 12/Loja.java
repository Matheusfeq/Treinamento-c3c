import java.util.Scanner;
import java.util.Dictionary;
import java.util.Hashtable;

public class Loja
{
    public static Scanner sc = new Scanner(System.in);
    
    public static void main(String[] args)
    {
        
        
        Dictionary mercadorias[] = new Dictionary[100];
        int contador = 0;
        while(true)
        {
            Dictionary mercadoria = new Hashtable();
            mercadoria.put("Nome ", InputLoja.obterNome());
            mercadoria.put("Qntd Mínima ", InputLoja.obterQuantidadeMinima());
            mercadoria.put("Qntd Máxima ",InputLoja.obterQuantidadeMaxima());
            mercadoria.put("Qntd Atual ",InputLoja.obterQuantidadeAtual(mercadoria.get("Qntd Máxima ")));
            mercadoria.put("Valor Unitário ",InputLoja.obterValorUnitario());
            mercadoria.put("Preço Total ", (double)mercadoria.get("Valor Unitário ")*(int)mercadoria.get("Qntd Atual "));
            if((int)mercadoria.get("Qntd Atual ") < (int)mercadoria.get("Qntd Mínima "))
            {
                mercadoria.put("Reposição ", "Sim");
            }
            else
            {
                mercadoria.put("Reposição ", "Não");
            }
            mercadorias[contador] = mercadoria;
            contador++;

            System.out.println("Gostaria de adicionar outra mercadoria?(S/N):");
            String flag = sc.next();
            if(flag.equals("N"))
            {
                break;
            }
        }
        for(int i = 0; i < contador; i++)
        {
            System.out.println(mercadorias[i]);
        }
    }
}