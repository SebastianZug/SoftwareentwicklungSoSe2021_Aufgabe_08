# SoftwareentwicklungSoSe2021_Aufgabe_08

## Bearbeitungzeit

SWE: 5. Juli - 9. Juli 2021 (Mm, BWM, ROB, BAI, BGIP, BBWL, BBL, MGIN)

## Beiträge



## Idee der Übung

Das Aufgabenblatt ist der Implementierung einer generischen Collection am Beispiel der Klasse `Set` gewidmet. Die Methoden der Klasse sind außerdem mit Hilfe des Test-Frameworks `xUnit` zu testen.

Schätzen Sie der Aufwand zur Lösung der Aufgaben im Voraus ab und teilen Sie die Aufgaben gleichmäßig untereinander auf. Verwenden Sie zur Organisation der Zusammenarbeit die GitHub-Features.

Organisieren Sie beide Projekte, die zu testende Klassenbibliothek und das Test-Projekt, in einer Solution.

## 1. Generische Collections

Erstellen Sie die generische Klasse `Set` zum Verwalten von Elementen einer Menge. Sinnvoll ist es, gleich zu Beginn eine Solution zu erstellen, die ein classlib-Projekt enthält (oder - wenn Sie die Klasse erst "manuell" testen wollen - ein ausführbares Projekt, das später in ein classlib-Projekt geändert wird). Dieser Solution kann dann ein Unittest-Projekt hinzugefügt werden.

Sie können dazu die *dotnet*-Kommandos nutzen, z.B.:

+ ```dotnet new sln -o unittesting```
+ ```dotnet new classlib -o SetCollectionLib``` (im Verzeichnis unittesting)
+ ```dotnet sln add SetCollectionLib/SetCollectionLib.csproj```

Die Klasse soll die Properties und Methoden des Interfaces `ICollection<T>` implementieren:

Properties:

+ `int Count` gibt die Anzahl der Elemente an, die in der Collection enthalten sind.

+ `bool IsReadOnly` gibt an, ob die Collection schreibgeschützt ist.

Methoden:

+ `void Add(T)` fügt der Collection ein Element hinzu.

+ `bool Remove(T)` entfernt das erste Vorkommen eines angegebenen Objekts aus der Collection.

+ `void Clear()` entfernt alle Elemente aus der Collection.

+ `bool Contains(T)` ermittelt, ob die Collection einen bestimmten Wert enthält.

+ `void CopyTo(T[], Int32)` kopiert die Elemente der Collection in ein Array, beginnend bei einem bestimmten Array-Index.

+ `IEnumerator<T> GetEnumerator()` gibt einen generischen Enumerator zurück, der die Collection durchläuft.

+ `IEnumerator GetEnumerator()` gibt einen nichtgenerischen Enumerator zurück, der die Collection durchläuft.

Verwenden Sie in der Klasse zum Speichern der Elemente ein  privates Feld vom Typ `List<T>`. Definieren Sie außerdem zum Verwalten von Elementen die angegebenen bzw. weitere sinnvolle Methoden. Nutzen Sie in den Methoden der Klasse die von der Klasse `List` zur Verfügung stehenden Properties und Methoden: `Count`, `Contains`, `Add`, `CopyTo`, `Remove`. Beachten Sie beim Implementieren der Methoden, dass alle Elemente einer Menge unterschiedlich sein müssen.

Hinweise zu `GetEnumerator()`:

+ Für die generische `GetEnumerator()`-Methode bietet sich die Verwendung der `yield return`-Anweisung an.

+ Die nichtgenerische `IEnumerable.GetEnumerator()`-Methode ist "historisch gewachsen" und wird nicht mehr verwendet, muss aber trotzdem implementiert werden. Im einfachsten Fall delegieren Sie sie an die generische Version (siehe auch: [implizite vs. explzite Interface-Implementierung](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/explicit-interface-implementation)):

```C#
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => GetEnumerator();
```

Definieren Sie in der Klasse weitere Properties und Methoden, z.B.:
`Cardinality`, `IsEmpty`, `IsSubsetOf()`, `Intersection()`, `Union()`

## 2. Testen mit xUnit

a)

Erstellen Sie ein weiteres Projekt zum Testen Ihrer Klassenbibliothek und fügen Sie das Projekt der Solution hinzu, z.B. mit den folgenden *dotnet*-Kommandos:

+ ```dotnet new xunit -o SetCollectionLib.Tests```
+ ```dotnet sln add SetCollectionLib.Tests/SetCollectionLib.Tests.csproj```

Fügen Sie die Klassenbibliothek anschließend dem Test-Projekt als Abhängigkeit hinzu:

+ ```dotnet add SetCollectionLib.Tests/SetCollectionLib.Tests.csproj reference SetCollectionLib/SetCollectionLib.csproj```

Erstellen Sie in der Test-Klasse für alle Methoden der Klasse `Set` jeweilige Testmethoden und führen Sie die Tests mit `dotnet test` aus. Verwenden Sie in den Testmethoden unterschiedliche Datentypen für die Elemente der Collection (z.B. `int` und `double`).

Nutzen Sie in den Testmethoden die Methoden der Klasse `Assert` wie `Assert.True` und `Assert.False` und die speziellen Collection-Methoden, wie z.B. `Assert.Empty`, `Assert.Equal<T>`, `Assert.Contains`, `Assert.DoesNotContain` etc.

Verwenden Sie, wo es sinnvoll ist, statt der einzelnen Tests mit dem Attribut `[Fact]` die Testreihen mit `Theory` und `InlineData`.

b)

Erstellen Sie einige Tests (z.B. für die Methoden `Intersection` und `Union`) mit den Objekten einer selbst definierten Klasse.

Geeignet wäre z.B. die "Stöckchen-Zahlen"-Klasse (s. Aufgabe 5.2), Sie können aber auch eine weitere Klasse dazu definieren. Testen Sie ebenfalls die Methoden dieser Klasse, in der "Stöckchen-Zahlen"-Klasse z.B. die überladenen Operatoren.

## Hinweise zu `xUnit` und Klasse `Assert`

[https://docs.microsoft.com/de-de/dotnet/core/testing/unit-testing-with-dotnet-test](https://docs.microsoft.com/de-de/dotnet/core/testing/unit-testing-with-dotnet-test)

[https://dotnetuniversity.com/testing-net-core-code-xunit/](https://dotnetuniversity.com/testing-net-core-code-xunit/)